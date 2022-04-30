#
# 函数作用域的LEGB顺序
#
# 1.什么是LEGB?
# L： local 函数内部作用域
# E: enclosing 函数内部与内嵌函数之间
# G: global 全局作用域
# B： build-in 内置作用
#
# python在函数里面的查找分为4种，称之为LEGB，也正是按照这是顺序来查找的
