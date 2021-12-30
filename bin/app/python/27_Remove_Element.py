from typing import List
class Solution:
    # 自力回答
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1

        nums[ans:] = ['_' for num in nums[ans:]]
        print(nums)
        return (ans)


ins = Solution()
nums = [3,2,2,3]
val = 3
ans = ins.removeElement(nums, 3)
print(ans)

