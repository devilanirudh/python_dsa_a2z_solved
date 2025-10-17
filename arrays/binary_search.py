from sys import implementation


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while(i<=j):
            mid = (i+j)//2
            if nums[mid] ==target:return mid
            elif target>nums[mid]:i = mid+1
            else:
                j = mid-1
        return -1


# method2

# recursive implementation
# def binary_search_recursion(n,low,high,target):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if n[mid] == target:
#         return mid
#     elif target>n[mid]:
#         return binary_search_recursion(n,mid+1,high,target)
#     return binary_search_recursion(n,low,mid-1,target)
    
# a = [1,2,3,4,5]
# print(binary_search_recursion(a,0,4,4))
        