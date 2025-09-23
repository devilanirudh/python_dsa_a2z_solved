def insertion(a):
    for i in range(1,len(a)):
        j = i-1
        key = a[i]
        while(j>=0 and a[j]>key):
            a[j+1] = a[j]
            j=j-1
        a[j+1]=key
    return a

a = [9,12,14,15,6,8,13]
print(insertion(a))
            