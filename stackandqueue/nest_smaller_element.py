def nse(ns):
    n = len(ns)
    nse=[0]*n
    st = []
    for i in range(n-1,-1,-1):
        while st and ns[st[-1]] >= ns[i]:
            st.pop()
        nse[i] = st[-1] if st else n
        st.append(i)
    
    return nse
    
    
    
    
arr = [4, 5, 2, 10, 8]    
print(nse(arr))