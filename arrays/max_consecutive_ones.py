class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_n = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count = count+1
            if count>max_n:
                max_n = count
            elif nums[i]!=1:
                count = 0
        return max_n
        