FROM python:3.9
WORKDIR /app

COPY main.py ./
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
