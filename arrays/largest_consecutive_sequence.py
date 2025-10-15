class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        co = 0
        longest = 1
        smaller = float('-inf')
        nums.sort()
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]-1==smaller:
                co = co+1
                smaller = nums[i]
            elif nums[i]==smaller:
                continue
            elif nums[i]!=smaller:
                smaller = nums[i]
                co = 1
            longest = max(longest,co)
        return longest
        

# method 2 using set data structure

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         s = set(nums)
#         longest = 0
#         for i in s:
#             if i-1 not in s:
#                 count = 1
#                 x = i
#                 while x+1 in s:
#                     x = x+1
#                     count = count +1
#                 longest = max(longest,count) 
#         return longest


