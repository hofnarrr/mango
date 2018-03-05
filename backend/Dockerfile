FROM python:3
EXPOSE 5000

ENV MANGO_MODE dev
RUN apt-get update && apt-get upgrade -y -qq
COPY . /mango-backend

WORKDIR /mango-backend
RUN pip install -r requirements.txt
RUN pip install --editable .

CMD mangoctl run -h 0.0.0.0 -p 5000
