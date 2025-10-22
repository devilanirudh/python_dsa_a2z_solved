class Solution:
    def singleNonDuplicate(self, nums):
        i = 1
        j = len(nums)-2
        n = len(nums)
        if (n ==1):return nums[0]
        if(nums[0]!=nums[1]):return nums[0]
        if(nums[n-1]!=nums[n-2]):return nums[n-1]
        while(i<=j):
            mid = (i+j)//2
            #you are in the left half
            if (nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            else:#you are in the right half
                if((mid%2==1 and nums[mid-1]==nums[mid]) or(mid%2==0 and nums[mid+1]==nums[mid] ) ):i = mid+1
                else:j = mid-1
        return -1
