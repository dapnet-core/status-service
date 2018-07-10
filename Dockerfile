FROM python:2

ADD status-service.py  /

RUN pip install Flask && pip install flask-restful

CMD [ "python", "./status-service.py" ]
