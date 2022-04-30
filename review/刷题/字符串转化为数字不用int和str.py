def get_res(s):
    index_list=[]
    char_list=[]
    sum=0
    for i in range (0,len(s)):
        index_list.append(len(s)-1-i)
        char_list.append(ord(s[i])-ord('0'))
        sum=sum+char_list[i]*(10**index_list[i])
    return sum


#ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。

print(get_res(s="23456"))