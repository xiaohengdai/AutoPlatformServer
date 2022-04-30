# Python之协程:https://www.cnblogs.com/russellyoung/p/python-zhi-xie-cheng.html
#Python threading中event的使用:https://blog.csdn.net/u012067766/article/details/79734630
#1、线程在程序中是独立的，并发的执行流，划分尺度小于进程，所有多线程程序的并发性高;
# 2、进程在执行过程中拥有独立的内存单元，而多个线程共享内存，可以极大地提高进程程序的运行效率;
#3、线程比进程具有更高的性能，由于同一个进程中的线程都有共性，多个线程共享同一个进程的虚拟空间，可以很容易实现通信。操作系统在创建进程中，必须为该进程分配独立内存空间，分配大量相关资源，但创建线程则简单得多。
#线程同步：Python之Event事件（简单教程）：https://blog.csdn.net/RNG_uzi_/article/details/109395624

#-*- coding:utf8 -*-
import gevent

def test(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

if __name__ == '__main__':
    g1 = gevent.spawn(test, 3)
    g2 = gevent.spawn(test, 3)
    g3 = gevent.spawn(test, 3)

    g1.join()
    g2.join()
    g3.join()
