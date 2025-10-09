def left_k_rotate(n,k):
    k %= len(n)
    temp = n[:k]
    for i in range(k,len(n)):
        n[i-k]=n[i]
    for i in range(0,k):
        n[-i-1]=temp[-i-1]
    return n

n = [1,2,3,4,5]
print(left_k_rotate(n,4))
    