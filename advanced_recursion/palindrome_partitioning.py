class Solution:
    def partition(self, s: str) -> List[List[str]]:
        a = []

        def palindrome(sub):
            i = 0
            j = len(sub) - 1
            while i < j:
                if sub[i] != sub[j]:
                    return False
                i += 1
                j -= 1
            return True

        def tp(i, b):
            if i == len(s):
                a.append(b[:])
                return

            for j in range(i, len(s)):
                sub = s[i:j+1]              
                if palindrome(sub):
                    b.append(sub)           
                    tp(j + 1, b)           
                    b.pop()                 

        tp(0, [])
        return a
