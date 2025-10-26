class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m*k > len(bloomDay)):
            return -1
        i = 0
        j = max(bloomDay)
        ans =0
        total_required = m*k
        def boq_pos(mid,k):
            consecutive = 0
            groups = 0
            for i in range(len(bloomDay)):
                if (bloomDay[i]-mid<=0):
                    consecutive += 1
                    if consecutive ==k:
                        groups +=1
                        consecutive = 0
                else:
                    if consecutive>=k:
                        groups +=1
                    consecutive = 0
            if consecutive >= k:
                groups += 1      
            return groups
        while(i<=j):
            mid = (i+j)//2
            if(boq_pos(mid,k)>=m):
                ans = mid
                j = mid-1
            else:
                i = mid+1
        return ans


        