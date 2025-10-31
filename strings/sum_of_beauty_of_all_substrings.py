class Solution:
    def beautySum(self, s: str) -> int:
        if not s: return 0
        total =0
        def beauty(s):
            if not s:return 0
            s1 = set(s)
            di = {}
            for ch in s1:
                di[ch]=s.count(ch)
            beauty = di[max(di,key=di.get)]-di[min(di,key=di.get)]
            return beauty
        def sub_s(s):
            nonlocal total
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    total = total+beauty(s[i:j])
        sub_s(s)    
        return total
         
