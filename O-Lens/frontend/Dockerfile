#Stage 1
FROM node:17-alpine as builder
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./

COPY ./ ./

RUN npm install
RUN npm run build

#Stage 2
FROM nginx:1.23.3 as production

WORKDIR /app

COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000
# Start nginx
ENTRYPOINT ["nginx", "-g", "daemon off;"]
