from typing import List
# 自力回答
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 配列の最初の文字列をprefixへ代入
        prefix = strs[0]
        strlen = len(strs[0])
        # 配列の2個目以降と文字列比較し、一致しなければ末尾から一文字ずつ削る。
        for str in strs[1:]:
            for i in range(0,strlen):
                # 前方一致判定
                if not str.startswith(prefix):
                    prefix = prefix[:-1]
        return prefix

# 垂直検索
class Solution_VerticalScanning:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 最も文字列の短い単語を取得する。
        prefix =""
        min_str= min(strs)
        strs.remove(min_str)
        stop_flag = False
        for i in range(0,len(min_str)):
            for str in strs:
                # i文字目を比較し、一致しなかった場合探索を打ち切る。
                if str[i] != min_str[i]:
                    stop_flag = True
                    break
            if stop_flag:
                break
            # 全て一致した場合はprefixへ追加
            prefix += min_str[i]
                
        return prefix
        
ins = Solution_VerticalScanning()
strs = ["flower","flow","flight"]
ans = ins.longestCommonPrefix(strs)
print(ans)