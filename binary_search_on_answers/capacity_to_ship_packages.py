class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        ans = j
        def check(m):
            group = 1
            su = 0
            for i in range(len(weights)):
                if(su+weights[i]>m):
                    su = 0
                    group +=1
                su = su+weights[i]
            return group     
        while(i<=j):
            mid = (i+j)//2
            if(check(mid)<=days):
                ans = mid
                j = mid-1
            else:
                i = mid+1
        return ans
        