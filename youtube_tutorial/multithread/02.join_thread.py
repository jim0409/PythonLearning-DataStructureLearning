import threading as td
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        print("Start the {}_th time".format(i))
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finsih\n')

def main():
    added_thread = td.Thread(target=thread_job, name='T1')
    thread2 = td.Thread(target=T2_job, name='T2')
    added_thread.start()
    thread2.start()

    # 沒有加入join，後面不會等前面。會導致還沒跑完10次T1 start程式就被取消了
    thread2.join()
    added_thread.join()
    
    print('all done\n')

if __name__ == "__main__":
    main()