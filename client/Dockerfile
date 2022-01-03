#https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html
#https://github.com/calaldees/frameworks_and_languages_module/blob/main/examples/client/vue_test/Dockerfile
FROM python:alpine

WORKDIR /app/

EXPOSE 8001

COPY . .

CMD ["python3", "-m", "http.server", "8001"]