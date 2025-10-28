# pythons replica of c++ priority queue

class Solution:
    def minimiseMaxDistance(self, arr, k):
        howmany = [0]*(len(arr)-1)
        from queue import PriorityQueue
        pq = PriorityQueue()
        for i in range(len(arr)-1):
            pq.put((-(arr[i+1]-arr[i]),-i))
        for i in range(k):
            tp = pq.get()
            secInd = -tp[1]
            howmany[secInd]+=1
            initialdiff = float(arr[secInd+1]-arr[secInd])
            newSection = float(initialdiff/(howmany[secInd]+1))
            pq.put((-newSection,-secInd))
        tp = pq.get()
        return -tp[0]
        
        
        
a = Solution()
arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
k = 9
print(a.minimiseMaxDistance(arr,k))


#binary search based minimisemaxdistance

# class Solution:
#     def minimiseMaxDistance(self, arr, k):
#         low = 0
#         high = 0
#         for i in range(len(arr)-1):
#             high = max(high,float((arr[i+1]-arr[i])))
#         def number_of_gas_stations(mid,arr):
#             count = 0
#             for i in range(1,len(arr)):
#                 numberinbetween = int((arr[i]-arr[i-1])/mid)
#                 if ((arr[i]-arr[i-1])/mid == numberinbetween*mid): #check for exact division
#                     numberinbetween-=1
#                 count += numberinbetween
#             return count
    
                
#         diff = 1e-6
#         while(high-low>diff):
#             mid = (low+high)/2.0
#             count = number_of_gas_stations(mid,arr)
#             if count>k:
#                 low = mid
#             else:
#                 high = mid
#         return high

# a = Solution()
# arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
# k = 9
# print(a.minimiseMaxDistance(arr,k))