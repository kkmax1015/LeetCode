from typing import List
import sys

class Solution:
    # 自力回答
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == target:
                index = i
                break
            elif nums[i] > target:
                if i == 0:
                    index = 0
                else:
                    index = i
                break

        return (index)

class Solution_Answer:
    # 二分探索
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left

ins = Solution_Answer()
nums = [1,3,5,6]
target = 2
ans = ins.searchInsert(nums, target)
print(ans)

