class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i = max(nums)
        j = sum(nums)
        def cou(mid):
            sub=1
            sub_sum = 0
            for i in range(len(nums)):
                if sub_sum+nums[i]<=mid:
                    sub_sum = sub_sum+nums[i]
                else:
                    sub +=1
                    sub_sum = nums[i]
            return sub
        while(i<=j):
            mid = (i+j)//2
            if (cou(mid)>k):
                i = mid+1
            else:j = mid-1
        return i
        