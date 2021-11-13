class Solution_ChangeString:
    # 文字列に変換した場合。非推奨
    def isPalindrome(self, x: int) -> bool:
        x_str = str(abs(x))
        x_reverse = x_str[::-1]
        if x_str==x_reverse and x > -1:
            return True
        else:
            return False

class Solution:
    # 数値の半分を逆整数にして比較する
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):  
            return False
        
        rev_x = 0
        while x > rev_x:
            rev_x = (rev_x*10) + (x%10)
            x = x//10

        if (x==rev_x) or (x==rev_x//10):
            return True
        else:
            return False

ins = Solution()
ans = ins.isPalindrome(1)
print(ans)