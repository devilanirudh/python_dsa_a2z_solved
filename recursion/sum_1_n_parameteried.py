def sum1(n,sum):
    a=n
    if (n<1):
        print(sum)
        return
    sum1(n-1,sum+n)
        
sum1(5,0)