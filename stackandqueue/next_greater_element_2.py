class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        for i in range(n):
            for j in range(i + 1, i + n):
                index = j % n
                if nums[index] > nums[i]:
                    res[i] = nums[index]
                    break
        
        return res

#stack based solution

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []
        for i in range((2*n-1),-1,-1):
            while(len(st)!=0 and st[-1]<=nums[i%n]):
                st.pop()
            if i<n:
                if len(st)!=0:
                    res[i]= st[-1]
            st.append(nums[i%n])
        return res
