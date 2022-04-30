# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false




class Solution():
    def verificate_palindrome(self,s):
        a=list(s)
        b=[]
        c=[]
        for i in range(0,len(a)):
            print(a[len(a) - 1 - i].isalnum())# isalnum() 方法检测字符串是否由字母和数字组成
            if a[len(a)-1-i].isalnum():
                print(i)
                b.append(a[len(a)-1-i])
            if a[i].isalnum():
                c.append(a[i])
        print("a:",a)
        print("b:",b)
        print("c:", c)
        a_str="".join(a).lower()
        b_str="".join(b).lower()
        c_str = "".join(c).lower()
        print("a_str:", a_str)
        print("b_str:",b_str)
        print("c_str:", c_str)
        if c_str==b_str:
            return True
        else:
            return False

solution=Solution()
# str="Aba"
str="A man, a plan, a canal: Panama"
res=solution.verificate_palindrome(str)
print("res:",res)
