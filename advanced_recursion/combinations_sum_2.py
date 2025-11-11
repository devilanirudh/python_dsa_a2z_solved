class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        a = []
        def com_1(can,tar,cur_su,idx,a,b):
            if cur_su==target:
                a.append(b[:])
                return 
            if cur_su>target or idx>=len(can):
                return
        
            b.append(can[idx])
            com_1(can,tar,cur_su+can[idx],idx+1,a,b)
            b.pop()

            next_idx = idx + 1
            while next_idx < len(can) and can[next_idx] == can[idx]:
                next_idx += 1
            com_1(can,tar,cur_su,next_idx,a,b)
        com_1(candidates,target,0,0,a,[])
        return a



        