# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1. clone the repo from the refer address in README.md                                     #
# 2. copy this Dockerfile and put in the repo folder as same as SimpleExampleServer.py      #
# 3. docker build -t websockerserver:v1 .                                                   #
# 4. docker run -it -p 8999:8999 -d websockerserver:v1                                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
FROM python:3.7.0-alpine

LABEL maintainer jim0409
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api
EXPOSE 8999
CMD python SimpleExampleServer.py --example chat --port 8999