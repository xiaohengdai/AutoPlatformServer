#合并两个有序数组

def get_res(s1,s2):
    if len(s1)==0:
        return s2
    if len(s2)==0:
        return s1
    point1=0
    point2=0
    s1_len=len(s1)
    s2_len=len(s2)
    s=[]
    while point1<s1_len and point2<s2_len:
        if s1[point1]<s2[point2]:
            s.append(s1[point1])
            point1=point1+1
        else:
            s.append(s2[point2])
            point2=point2+1
    if point1==s1_len:
        s.extend(s2[point2:])
    elif point2==s2_len:
        s.extend(s1[point1:])

    return s

print(get_res(s1=[3,4],s2=[4,6,7]))


