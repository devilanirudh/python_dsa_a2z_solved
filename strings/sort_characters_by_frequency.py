class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        max_heap=[]
        f = list(set(s))
        print(f)
        l=[]
        for ch in f:
            a = s.count(ch)
            heapq.heappush(max_heap,(-a,ch))
        
        for ch in f:
            a = heapq.heappop(max_heap)
            l.append(a[1]*-a[0])

        return ''.join(l)



# this will give tle because of the time complexity of the heapq.heappush and heapq.heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        max_heap=[]
        l=[]
        for ch in s:
            a = s.count(ch)
            heapq.heappush(max_heap,(-a,ch))
        
        for i in range(len(s)):
            a = heapq.heappop(max_heap)
            l.append(a[1])
        

        return ''.join(l)