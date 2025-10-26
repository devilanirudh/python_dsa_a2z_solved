class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        i = 1
        j = max(nums)
        ans = 0
        def divi(m):
            total = 0
            for i in range(len(nums)):
                import math
                total = total+(math.ceil(nums[i]/mid))
            return total
        while(i<=j):
            mid = (i+j)//2
            if(divi(mid)<=threshold):
                ans = mid
                j = mid-1
            else:
                i = mid+1
        return ans