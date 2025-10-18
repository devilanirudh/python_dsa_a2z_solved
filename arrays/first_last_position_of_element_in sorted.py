class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums,target):
            i = 0
            j = len(nums)-1
            ans = len(nums)
            while(i<=j):
                mid = (i+j)//2
                if nums[mid]>=target:
                    ans = mid
                    j = mid -1
                else:i = mid+1
            return ans
        def upper_bound(nums,target):
            i = 0
            j = len(nums)-1
            ans = len(nums)
            while(i<=j):
                mid = (i+j)//2
                if nums[mid]>target:
                    ans = mid
                    j = mid -1
                else:i = mid+1
            return ans
        res = [-1, -1]
        if not nums:
            return res

        lb = lower_bound(nums, target)
        if lb < len(nums) and nums[lb] == target:
            ub = upper_bound(nums, target)
            res[0] = lb
            res[1] = ub - 1

        return res