def hash(a):
    c = max(a)
    hash_d = [0]*(c+1)
    for i in range(len(a)):
        hash_d[a[i]] = hash_d[a[i]]+1
    return hash_d

def freq(hash_d,b):
    return hash_d[b]

a = [1,2,3,1,2,2,2,2,2]
d = hash(a)
print(freq(d,1))


    
    