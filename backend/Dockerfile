FROM python:3

WORKDIR /mango-backend
ADD . /mango-backend

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "run.py" ]
