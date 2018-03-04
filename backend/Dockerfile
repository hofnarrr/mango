FROM python:3

WORKDIR /mango-backend
ADD . /mango-backend

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "mango.app:create_app()"
