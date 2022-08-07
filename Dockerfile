FROM python:3.9-slim-buster
RUN apt update && apt upgrade -y
RUN mkdir /app/
WORKDIR /app/

COPY . /app/
RUN pip3 install -U -r requirements.txt
COPY . /app/startup

CMD ["python3", "startup"]
