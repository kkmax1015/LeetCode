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
            
        
class Solution_answer:
    def romanToInt(self, s: str) -> int:

        # 記号と値のdictを作成しておく
        dict_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        before_value = 0
        # 文字列を右端から一文字ずつ切り出し
        for split_s in s[::-1]:
            value = dict_value.get(split_s)
            # ローマ数字は基本的に大きい数字から記載される。
            # 一部の組み合わせ(IV:4など)は例外で小さい数字が先に来るので、前の数字より小さい場合は減算する。
            if value >= before_value:
                ans += value
            else:
                ans -= value
            before_value = value
        return ans

ins = Solution_answer()
ans = ins.romanToInt('MCMXCIV')
print(ans)