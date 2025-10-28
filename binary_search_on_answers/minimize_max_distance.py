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