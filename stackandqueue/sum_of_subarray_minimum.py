class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:


        def findnse(ns):
            n = len(ns)
            nse=[0]*n
            st = []
            for i in range(n-1,-1,-1):
                while st and ns[st[-1]] >= ns[i]:
                    st.pop()
                nse[i] = st[-1] if st else n
                st.append(i)
            
            return nse

        def findpse(arr):
            n = len(arr)
            psee =[0]*n
            st = []
            for i in range(n):
                while st and arr[st[-1]]>arr[i]:
                    st.pop()
                psee[i]=st[-1] if st else -1
                st.append(i)
            
            return psee
        n = len(arr)
        nse = findnse(arr)
        pse = findpse(arr)
        total = 0
        mod = (10**9)+7

        for i in range(n):
            left = i-pse[i]
            right = nse[i]-i
            total = (total+(right*left*arr[i])%mod)%mod
        return total