def sq(n):
    i = 0
    j = n
    ans =1
    while(i<=j):
        mid = (i+j)//2
        if ((mid*mid)<=n):
            ans = mid
            i = mid+1
        else:
            j = mid-1
    return ans
print(sq(28))