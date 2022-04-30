# 6、请说下什么是闭包函数？
# 完成的闭包必须包含以下三个特性：函数中必须嵌套一个函数；外层函数返回值是内层函数的函数名；内存嵌套函数对外层作用率，有非全局变量的引用；
# 简单来说闭包函数，第二个返回的不仅仅是一个简单的函数，这个函数它还呆了一个封闭的作用域；

import time


def run_time(func):
    def wrapper(*args,**kwargs):
        print("time.time():",time.time())
        func(*args,**kwargs)
    return wrapper

@run_time
def test_time(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)
    pass


test_time(1,2,key='value')





