class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        j = k+len(arr)
        ans = 0
        def missing_before(m):
            miss = 0
            for i in range(mid):
                if(i not in  arr):
                    miss += 1
            return miss               
        while(i<=j):
            mid = (i+j)//2
            if (missing_before(mid)<=k):
                ans = mid
                i = mid+1
            else:
                j = mid-1
        return ans