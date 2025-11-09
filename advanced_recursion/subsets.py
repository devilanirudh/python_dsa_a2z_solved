class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for num in nums:
            a += [subset + [num] for subset in a]
        return a


# bitmask method

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        a = []
        for i in range(pow(2,n)):
            sub=[]
            for j in range(n):
                if(i&(1<<j)):
                    sub.append(nums[j])
            a.append(sub)
        return a
        

#using backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i,a):
            if i==len(nums):
                result.append(a[:])
                return 
            a.append(nums[i])
            backtrack(i+1,a)
            a.pop()
            backtrack(i+1,a)
        backtrack(0,[])
        return result
