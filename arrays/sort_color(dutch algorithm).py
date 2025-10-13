class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 = count_0+1
            elif nums[i] == 1:
                count_1 = count_1+1
            elif nums[i] == 2: 
                count_2 = count_2+1
        for i in range(count_0):nums[i]=0
        for i in range(count_0, count_0 + count_1):nums[i]=1
        for i in range(count_0 + count_1, count_0 + count_1 + count_2):nums[i]=2

        

# method 2

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         low =0
#         mid=0
#         high=len(nums)-1
#         while(mid<=high):
#             if nums[mid] == 0 :
#                 nums[low],nums[mid]=nums[mid],nums[low]
#                 low=low+1
#                 mid=mid+1
#             elif nums[mid] ==1:
#                 mid=mid+1
#             elif nums[mid] ==2:
#                 nums[mid],nums[high]=nums[high],nums[mid]
#                 high=high-1

        