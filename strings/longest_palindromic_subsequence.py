class Solution:
    def longestPalindrome(self, s: str) -> str:
        su=""
        def is_palindrome(i,j):
            while(i<j):
                if(s[i]!=s[j]):return False
                i+=1
                j-=1
            return True
        def sub_s(s):
            nonlocal su
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    if len(s[i:j])>len(su):
                        if is_palindrome(i,j-1):
                            su = s[i:j]
        
        sub_s(s)
        return su