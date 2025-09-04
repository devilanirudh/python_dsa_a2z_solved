def count(n):
    start=0
    while(n>0):
        start+=1
        n=n//10
    return(start)
print(count(123))