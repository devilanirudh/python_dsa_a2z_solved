class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):return False
        a = 0
        b=0
        for ch,ch1 in zip(s,t):
            a = a+ord(ch)
            b = b+ord(ch1)
            if (s.count(ch)!=t.count(ch)):
                return False
            if (ch not in t):
                return False
        return a==b