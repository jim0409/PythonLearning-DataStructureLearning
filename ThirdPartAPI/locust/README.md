# intro
Another tools for loading test


# quick start
1. set up nginx for test target
> docker run --rm --name nginx -p 80:80 -d nginx:1.13.7
2. set up docker-compose for locustio
> docker-compose up --scale worker=4


# drop down
1. stop nginx
> docker stop nginx
2. stop docker-compose
> docker-compose down -v


# refer:
### example of locustfile
- https://blog.techbridge.cc/2019/05/29/how-to-use-python-locust-to-do-load-testing/

### example of docker-compose setup env
- https://docs.locust.io/en/stable/running-locust-docker.html
