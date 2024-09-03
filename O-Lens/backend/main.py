from fastapi import FastAPI, UploadFile, File
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from keras.applications.resnet import decode_predictions, preprocess_input
from keras.utils import img_to_array
from tensorflow import expand_dims
from keras.applications.resnet import ResNet50


app = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

model = ResNet50(weights='imagenet')


def get_image(file):
    return Image.open(file).convert("RGB")


@app.post("/")
async def image_prediction(file: UploadFile = File(...)):

    img = get_image(file.file)

    img = img.resize((224, 224))

    img_array = img_to_array(img)
    img_array = expand_dims(img_array, 0)
    img_array = preprocess_input(img_array)

    pred = model.predict(img_array)

    result = decode_predictions(pred, 2)[0]

    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["image_prediction"] = res[1]
        resp["image_prediction_confidence"] = f"{res[2]*100:0.2f}%"

        response.append(resp)

    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
