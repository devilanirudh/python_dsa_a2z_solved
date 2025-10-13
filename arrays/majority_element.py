class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        heap_max={}
        for i in range(len(nums)):
            if nums[i] in heap_max:
                h = heap_max.get(nums[i])+1
                heap_max.update({nums[i]:h})
            elif nums[i] not in heap_max:
                heap_max.update({nums[i]:1})
        y = max(heap_max, key=heap_max.get)
        return y


# method-2 

# moores voting algorithm
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         el=0
#         count =0
#         for i in range(len(nums)):
#             if count ==0:
#                 count=1
#                 el=nums[i]
#             elif nums[i]==el:
#                 count = count+1
#             else:
#                 count = count-1
#         return el

        
        