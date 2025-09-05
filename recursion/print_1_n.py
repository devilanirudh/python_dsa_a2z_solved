def rec(n):
    if(n>0):
        n=n-1
        rec(n)
        print(n)
rec(5)