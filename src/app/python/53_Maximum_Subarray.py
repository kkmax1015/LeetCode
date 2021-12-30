from typing import List

class Solution:
    # 自力回答
    ## 総当たり
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                work_sum = sum(nums[i:j+1])
                if ans < work_sum:
                    ans = work_sum

        return ans

class Solution_DynamicProgramming:
    # 動的計画法
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = current_subarray = nums[0]
        for i in range(1,len(nums)):
            current_subarray = max(nums[i], current_subarray + nums[i])
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray

ins = Solution_DynamicProgramming()
nums = [-2,1]
ans = ins.maxSubArray(nums)
print(ans)

