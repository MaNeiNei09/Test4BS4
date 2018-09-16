#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
# 多线程计算数字的平方
# date = 2018.09.16
# author = zbh
'''


import threading
import time
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    results = []

    print('-----------------------------')

    for i in range(3):
        t = threading.Thread(target=job, args=(data[i], q))
        print('Thread T%s starts,for list data%s=%s,the results is:' %(i,i,data[i]))
        start = time.time()
        t.start()
        threads.append(t)
        print(q.get())
        stop = time.time()
        cost = stop - start
        print('Thread T%s finish,it cost %1.20f seconds'%(i,cost))
        print('-----------------------------')

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    s_t = time.time()
    multithreading()
    print('cost:%1.8f s'%(time.time()-s_t))