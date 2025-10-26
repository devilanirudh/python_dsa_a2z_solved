class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def tt(k,n):
            t = 0
            for i in range(len(n)):
                import math
                t = t+math.ceil((n[i]/k))
            return t
        i = 1
        j = max(piles)
        fi = j
        while(i<=j):
            mid = (i+j)//2
            ti = tt(mid,piles)
            if (ti<=h):
                fi = mid
                j = mid-1
            else:
                i = mid+1
        return fi
    
                