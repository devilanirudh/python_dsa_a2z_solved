class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        def sub(idx,b):
            if idx == len(nums):
                a.append(b[:])
                return

            b.append(nums[idx])
            sub(idx+1,b)
            b.pop()
            next_idx = idx+1
            while(next_idx<len(nums) and nums[idx]==nums[next_idx]):
                next_idx+=1
            sub(next_idx,b)
        sub(0,[])
        return a 

        