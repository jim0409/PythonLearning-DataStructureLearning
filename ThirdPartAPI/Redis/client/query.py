# step 1. install redis client for python , pip install redis-py
# step 2. install docker for redis container
# run redis container with `docker run --name some-redis -p 6379:6379 -d redis`
# (ps: need to open port)
# for more ref; http://www.runoob.com/redis/redis-data-types.html
import redis

r = redis.StrictRedis(
    host='0.0.0.0',
    port=6379,
    db=0
    # password='password'
)

r.set('foo', 'bar')
value = r.get('foo')
print("%s" % value)
