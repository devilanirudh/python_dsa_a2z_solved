class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        
        def helper(l, r):
            if l >= r:  
                return True
            if filtered[l] != filtered[r]:
                return False
            return helper(l + 1, r - 1) 

        return helper(0, len(filtered) - 1