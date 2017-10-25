#-*- coding: utf-8 -*-
#!/usr/bin/python

import _thread
import time

def Threadfun(string, sleeptime, *args):
    while(True):
        print ('{0}_{1}\n'.format(string, sleeptime))
        time.sleep(sleeptime)

if __name__ == "__main__":
    for i in range(1,5):
        _thread.start_new_thread(Threadfun, ("ThreadFun", i))
    while(True):
        print ('MainThread {0}'.format(_thread.get_ident()))
        time.sleep(1)



