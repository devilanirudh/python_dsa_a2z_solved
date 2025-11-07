class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = n
        if nn<0:
            nn = -1*nn
        ans = 1.0
        while(nn!=0):
            if nn%2==0:
                x = x * x
                nn = nn//2
            else:
                ans = ans*x
                nn = nn-1
        if n<0:
            return 1/ans
        return ans
        
        



            
        