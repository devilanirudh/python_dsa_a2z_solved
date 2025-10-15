class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                index = i
                break
        if index == -1:
            nums.reverse()
            return
        for i in range(len(nums)-1,index,-1):
            if nums[i]>nums[index]:
                nums[i],nums[index] = nums[index],nums[i]
                break
        left = index+1
        right = len(nums)-1
        while(left<right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
