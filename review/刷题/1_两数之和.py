# 1. 两数之和：https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self,nums,target):
        res=[]
        nums_len=len(nums)
        for i in range(0,nums_len):
            for j in range(i+1,nums_len):
                if (nums[i]+nums[j])==target:
                    res.append(i)
                    res.append(j)
                    return res
        return res

sol=Solution()
res=sol.twoSum(nums=[2,7,11,15],target=9)
print("res:",res)

res=sol.twoSum(nums=[3,2,4],target=6)
print("res:",res)

res=sol.twoSum(nums=[3,3],target=6)
print("res:",res)

