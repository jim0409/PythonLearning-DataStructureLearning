FROM python:3.7.0-alpine
ENV PYTHONUNBUFFERED 1

# add code into container
ADD main.py .

# add requirements into container
ADD requirements.txt .

# copy entrypoint into root folder
COPY ./entrypoint.sh /

# install depends pacakage for container
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev && \
    pip install -r requirements.txt && \
    apk del .build-deps


RUN set -eux; chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]