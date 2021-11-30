#https://falconframework.org/
#https://github.com/calaldees/mame-7z/blob/25a25be22d68799552830516c95825b51fea58c2/catalog/catalog.py#L227
FROM python:alpine

EXPOSE 8000
WORKDIR /app/

# Install gunicorn & falcon
RUN pip install gunicorn falcon

# Add demo app
COPY . .


ENTRYPOINT [ "gunicorn","-b", "0.0.0.0:8000", "app:api" ]

