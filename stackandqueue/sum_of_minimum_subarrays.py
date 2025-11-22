class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        m = []
        b = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                a = min(arr[i:j])
                m.append(a)
        b = sum(m)
        r = (10**9)+7
        return b%r