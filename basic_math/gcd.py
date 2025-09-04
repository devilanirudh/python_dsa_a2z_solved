def gcd(a,b):
    gcd = 0
    for i in range(1,b):
        if(a%i==0 & b%i==0):
            gcd = i
        else:
            pass
    return gcd
            
print(gcd(3,6))