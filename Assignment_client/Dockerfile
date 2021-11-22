#https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html
FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /Assignment_client
RUN npm install
RUN npm run build
EXPOSE 8000