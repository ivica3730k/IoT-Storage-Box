FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app
WORKDIR /app/app
RUN pip3 install -r requirements.txt
