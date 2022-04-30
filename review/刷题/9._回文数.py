# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        len_str_x=len(str_x)
        for i in range (0,len_str_x):
            if (str_x[i]!=str_x[len_str_x-i-1]):
                return False
        return True

sol=Solution()
res=sol.isPalindrome(x=121)
print(res)
res=sol.isPalindrome(x=-121)
print(res)
res=sol.isPalindrome(x=10)
print(res)
res=sol.isPalindrome(x=-101)
print(res)