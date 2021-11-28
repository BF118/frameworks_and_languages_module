#https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html
#https://github.com/calaldees/frameworks_and_languages_module/blob/main/examples/client/vue_test/Dockerfile
FROM nginx:alpine

ENV PATH_NGINX_SERVE=/usr/share/nginx/html
RUN curl https://unpkg.com/vue@next -L -o ${PATH_NGINX_SERVE}/vue.js
COPY . ${PATH_NGINX_SERVE}