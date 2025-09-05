def rec(n):
    if(n>0):
        print(n)
        n=n-1
        rec(n)
rec(5)