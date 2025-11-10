class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []
        def com(can,tar,cur_su,idx,a,b):
            if cur_su == target:
                a.append(b[:])
                return
            if cur_su > target or idx >= len(can):
                return
            b.append(can[idx])
            com(can,tar,cur_su+can[idx],idx,a,b)
            b.pop()
            com(can,tar,cur_su,idx+1,a,b)
        
        com(candidates,target,0,0,a,[])
        return a



        