#https://falconframework.org/
FROM python:alpine

EXPOSE 8000
WORKDIR /app/

# Install gunicorn & falcon
RUN pip install gunicorn falcon

# Add demo app
COPY . .

CMD [ "python3","app.py" ]

