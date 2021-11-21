from typing import List
# 自力回答
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        strlen = len(strs[0])
        for str in strs[1:]:
            for i in range(0,strlen):
                if not str.startswith(prefix):
                    prefix = prefix[:-1]
        return prefix
        
ins = Solution()
strs = ["flower","flow","flight"]
ans = ins.longestCommonPrefix(strs)
print(ans)