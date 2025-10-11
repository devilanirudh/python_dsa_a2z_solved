class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_t = (n*(n+1))/2
        sum_arr = 0
        for i in range(len(nums)):
            sum_arr = sum_arr+nums[i]

        return (int(sum_t-sum_arr))
        