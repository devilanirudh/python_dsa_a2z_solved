class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        exist_dic = {')':'(','}':'{',']':'['}
        for ch in s:
            if ch in exist_dic:
                if a and a[-1]==exist_dic[ch]:
                    a.pop()
                else:return False
            else:
                a.append(ch)
        return len(a)==0
        