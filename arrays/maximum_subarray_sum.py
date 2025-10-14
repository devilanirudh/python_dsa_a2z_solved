class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        sub_arr = 0
        for i in range(len(nums)):
            sub_arr = max(nums[i], sub_arr + nums[i])
            max_sum = max(max_sum,sub_arr)
        return max_sum
        