def isprime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
print(isprime(2)) #True
print(isprime(4)) #False
print(isprime(7)) #True
print(isprime(9)) #False
print(isprime(11)) #True
print(isprime(13)) #True
print(isprime(15)) #False
print(isprime(17)) #True
print(isprime(19)) #True
print(isprime(21)) #False