#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
# 线程锁
# date = 2018.09.16
# author = zbh
'''


import threading
import time

def job1():
    global A,lock
    lock.acquire()
    t_s = time.time()
    print('-----Job1 start--------')
    for i in range(10):
        A += 1
        print('Job1 No.%d is: %d'%(i, A))
    t_f = time.time()
    cost = t_f - t_s
    print('Cost: %1.15f s' % cost)
    print('-----Job1 finishi------')
    print('\n')
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    t_s = time.time()
    print('-----Job2 start--------')
    for i in range(10):
        A += 10
        print('Job2 No.%d is: %d'%(i, A))
    t_f = time.time()
    cost = t_f - t_s
    print('Cost: %1.15f s' % cost)
    print('-----Job2 finishi-----')
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
