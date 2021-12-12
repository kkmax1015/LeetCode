class Solution:
    # 自力回答
    def isValid(self, s: str) -> bool:
        if not len(s)%2==0:
            return False
        dict_type = {'(':')', '{':'}', '[':']'}
        bracket = ''
        close_brackets = [')', '}', ']']
        open_brackets =[]
        for char in s:
            if char in close_brackets:
                if dict_type.get(bracket) == char:
                    del open_brackets[-1]
                    if len(open_brackets) > 0:
                        bracket = open_brackets[-1]
                    else:
                        bracket = ''
                else:
                    return False
            else:
                open_brackets.append(char)
                bracket = open_brackets[-1]
        if len(open_brackets)==0:
            return True
        else:
            return False


ins = Solution()
s = "(){}}{"
ans = ins.isValid(s)
print(ans)