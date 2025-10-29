class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = []
        for ch in s:
            if ch == '(':
                if count > 0:
                    res.append(ch)
                count += 1
            elif ch == ')':
                count -= 1
                if count > 0:
                    res.append(ch)
        return ''.join(res)

