# base image
FROM python:3.11-alpine

# set working directory
ADD . /app
WORKDIR /app

# add and install requirements
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

# run server
CMD ["flask", "run", "--host", "0.0.0.0"]
