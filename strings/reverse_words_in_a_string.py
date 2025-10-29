class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.strip().split()
        res=[]
        for ch in reversed(s1):
            res.append(ch)
        return ' '.join(res)