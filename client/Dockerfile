#https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html
FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app


# install project dependencies
RUN npm install vue

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
#RUN npm run build

EXPOSE 8000
CMD [ "http-server", "dist" ]