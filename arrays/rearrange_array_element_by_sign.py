class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [0] * len(nums)
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]>0 and pos<len(nums):
                a[pos] = nums[i]
                pos=pos+2
            elif nums[i]<0 and neg<len(nums):
                a[neg] = nums[i]
                neg=neg+2
        return a


        