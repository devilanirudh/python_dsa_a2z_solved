def sub_s(a,b,n,b1):
    if b == b1:
        return 1
    if a==n or b>b1:
        return 0

    l = sub_s(a+1,b+a1[a],n,b1)
    r = sub_s(a+1,b,n,b1)
    return l+r
    

a1 = [1,2,3]
n = len(a1)
su = 3
print(sub_s(0,0,n,su))
