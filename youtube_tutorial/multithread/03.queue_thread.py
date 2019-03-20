import threading as td
import time
from queue import Queue

def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading(data):
    q = Queue()
    threads = []
    # 用來儲存線程從queue拿出來的值
    results = []

    for i in range(4):
        # args 表示要丟進job裡面的參數
        t = td.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__ == "__main__":
    data =[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    multithreading(data)