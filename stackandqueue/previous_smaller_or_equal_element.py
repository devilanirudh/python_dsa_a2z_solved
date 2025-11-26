def psee(arr):
    n = len(arr)
    psee =[0]*n
    st = []
    for i in range(n):
        while st and st[-1]>arr[i]:
            st.pop()
        psee[i]=st[-1] if st else -1
        st.append(i)
    
    return psee
    
arr = [3,2,5,7]
print(psee(arr))
        