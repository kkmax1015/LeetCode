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

class Solution_Answer:
    # スタックを使用する。
    # 基本は自力回答と考え方は同じ
    def isValid(self, s: str) -> bool:
        if not len(s)%2==0:
            return False
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for char in s:
            # 閉じ括弧の場合
            if char in mapping:
                # 現在の開いている記号のトップを取得
                top_element = stack.pop() if stack else '#'
                # 対応する閉じ括弧でなければfalse
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack 
            


ins = Solution()
s = "(){}}{"
ans = ins.isValid(s)
print(ans)