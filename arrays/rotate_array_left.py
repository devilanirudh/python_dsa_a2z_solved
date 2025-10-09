def left_rotate(n):
    temp = n[0]
    for i in range(1,len(n)):
        n[i-1] = n[i]
    n[-1]=temp
    return n

n = [1,2,3,4,5]
print(left_rotate(n))