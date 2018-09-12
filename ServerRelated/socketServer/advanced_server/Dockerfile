# need to optimize container images either size or performance
FROM python:2.7.10

LABEL maintainer jim
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api
CMD python chat.py