FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3 -m pip install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@7.23.0
RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN pip3 install --use-deprecated=legacy-resolver -r requirements.txt
CMD python3 main.py
