import requests
import time
import asyncio

# url = 'https://www.google.com.tw/'

# start_time = time.time()

# def send_req(url):
#     t = time.time()
#     print("Send a request at",t-start_time,"seconds.")
#     res = requests.get(url)
#     t = time.time()
#     print("Receive a response at",t-start_time,"seconds.")
    

# for i in range(10):
#     send_req(url)


# url = 'https://www.google.com.tw/'
url = 'http://127.0.0.1'
loop = asyncio.get_event_loop()

start_time = time.time()

async def send_req(url):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = await loop.run_in_executor(None,requests.get,url)

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

tasks = []

for i in range(1000):
    task = loop.create_task(send_req(url))
    tasks.append(task)

a=time.time()
loop.run_until_complete(asyncio.wait(tasks))
b=time.time()

print(b-a)

# 166~200 request persecond
