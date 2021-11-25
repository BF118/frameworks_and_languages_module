#https://falconframework.org/
#https://github.com/calaldees/mame-7z/blob/25a25be22d68799552830516c95825b51fea58c2/catalog/catalog.py#L227
FROM python:alpine

EXPOSE  8000

RUN pip install gunicorn falcon

COPY ./app /app
WORKDIR /app 


CMD ["gunicorn", "-b", "0.0.0.0:8000", "sample:api"]
