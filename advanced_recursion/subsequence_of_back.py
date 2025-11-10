def sub_s(a,b,n,b1):
    if b == n:
        print(a)
        b1.append(a[:])
        return
    a.append(a1[b])
    sub_s(a,b+1,n,b1)
    a.remove(a1[b])
    sub_s(a,b+1,n,b1)
    return b1
    

a1 = [1,2,3]
n = len(a1)
a=[]
b1 = [[]]
print(sub_s(a,0,n,b1))
