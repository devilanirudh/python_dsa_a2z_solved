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


        