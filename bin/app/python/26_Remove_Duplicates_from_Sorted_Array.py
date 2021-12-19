from typing import List
class Solution:
    # 自力回答
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = set(nums)
        nums.sort()
        return len(nums)

ins = Solution()
nums = [1,1,2]
ans = ins.removeDuplicates(nums)
print(ans)