class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 1
        j = len(nums)-2
        n = len(nums)
        if len(nums)==1:return 0
        if nums[0]>nums[1]:return 0
        if nums[n-1]>nums[n-2]:return n-1
        while(i<=j):
            mid = (i+j)//2
            if (nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]):return mid
            elif (nums[mid-1]<nums[mid]):i=mid+1
            else:j = mid-1
        return -1

        !
        