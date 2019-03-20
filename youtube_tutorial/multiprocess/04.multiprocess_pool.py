import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=2)
    # 進程中會使用到全部的cpu
    res = pool.map(job, range(10))
    print(res)

    # 一次只能在一個進程中算一個cpu
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == "__main__":
    multicore()