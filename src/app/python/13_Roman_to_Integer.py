class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        if 'IV' in s:
            ans += 4
            s = s.replace('IV', '')
        if 'IX' in s:
            ans += 9
            s = s.replace('IX', '')
        if 'XL' in s:
            ans += 40
            s = s.replace('XL', '')
        if 'XC' in s:
            ans += 90
            s = s.replace('XC', '')
        if 'CD' in s:
            ans += 400
            s = s.replace('CD', '')
        if 'CM' in s:
            ans += 900
            s = s.replace('CM', '')

        for split_s in s:
            if split_s in 'I':
                ans += 1
            if split_s in 'V':
                ans += 5
            if split_s in 'X':
                ans += 10
            if split_s in 'L':
                ans += 50
            if split_s in 'C':
                ans += 100
            if split_s in 'D':
                ans += 500
            if split_s in 'M':
                ans += 1000
        return ans
            
        




ins = Solution()
ans = ins.romanToInt('MCMXCIV')
print(ans)