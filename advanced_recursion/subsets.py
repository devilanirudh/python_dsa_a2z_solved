class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for num in nums:
            a += [subset + [num] for subset in a]
        return a
        