class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        elif len(s)%2!=0:
            return False
        A={'{':'}','[':']','(':')'}
        stack=list()
        stack.append(s[0])
        for i in range (1,len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i]!=A.get(stack[-1]):
                stack.append(s[i])
            else:
                stack.pop()
        print("stack:",stack)
        if len(stack)==0:
            return True
        else:
            return False

#
sol=Solution()
# res=sol.isValid(s="()")
# print(res)
# res=sol.isValid(s="()[]{}")
# print(res)
# res=sol.isValid(s="(]")
# print(res)
# res=sol.isValid(s="([)]")
# print(res)
# res=sol.isValid(s="{[]}")
# print(res)
#
res=sol.isValid(s="(([]){})")
print(res)

