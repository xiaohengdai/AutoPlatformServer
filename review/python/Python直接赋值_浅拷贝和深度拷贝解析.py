#直接赋值：其实就是对象的引用（别名）。
#浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
#深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

a={1:[1,2,3]}
b=a
print("id(a):",id(a))
print("id(b):",id(b))
#id(a)和id(b)相等

b=a.copy()
print("a:",a)
print("b:",b)
a[1].append(4)
print("a:",a)
print("b:",b)
print("id(a):",id(a))
print("id(b):",id(b))

import copy

c=copy.deepcopy(a)
print("a:",a)
print("c:",c)
a[1].append(5)
print("a:",a)
print("c:",c)
print("id(a):",id(a))
print("id(c):",id(c))