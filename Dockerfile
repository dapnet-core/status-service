FROM python:3

ADD status-service.py  /

RUN pip3 install flask && pip3 install flask-restful

# private and public mapping
EXPOSE 5000

CMD [ "python", "./status-service.py" ]
