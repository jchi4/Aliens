# syntax=docker/dockerfile:1
FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update -y && \
    apt-get install -y python -pip python-dev && \
    pip install --upgrade pip 

WORKDIR /website

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000 80 8080 443 22
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]