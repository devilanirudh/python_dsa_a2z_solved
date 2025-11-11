class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        a = []
        def com_3(i,cur_su,b):
            if len(b)==k:
                if cur_su == n:
                    a.append(b[:])
                    return
            if len(b)>k or cur_su>n or i>=len(nums):
                return
            
            b.append(nums[i])
            com_3(i+1,cur_su+nums[i],b)
            b.pop()
            com_3(i+1,cur_su,b)
        com_3(0,0,[])
        return a


        