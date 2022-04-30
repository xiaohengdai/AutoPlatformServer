class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums: List[int], target: int) -> List[int]:
            l, r = 0, len(nums)  # 左闭右开不需要减1
            while (l < r):
                m = l + (r - l) // 2  # 不能用右移实现 会超时，具体细节不清楚
                if (nums[m] >= target):  # 目标在左边区域
                    r = m
                else:  # 如果目标在右区域，左边界右移
                    l = m + 1
            return l

        def right_bound(nums: List[int], target: int) -> List[int]:
            l, r = 0, len(nums)  # 左闭右开不需要减1
            while (l < r):
                m = l + (r - l) // 2
                if (nums[m] > target):  # 目标在左边区域
                    r = m
                else:  # 小于等于即要更新左边界
                    l = m + 1
            return l

        lb = left_bound(nums, target)
        rb = right_bound(nums, target) - 1  # 开区间需要减1

        if (not nums): return [-1, -1]  # 为空检测
        if (lb == len(nums) or nums[lb] != target): return [-1,
                                                            -1]  # target不存在检测，or前表示搜索完未找到目标，or后虽然target在数组的范围内，但不存在该值。例如数组{3,6,7},target为5，此时应该返回{-1, -1}
        return [lb, rb]


