def largest(a):
    largest = a[0]
    for i in range(1,len(a)):
        if a[i]>largest:
            largest = a[i]
    return largest

a = [1,2,3,4,5,10,6,7,5]
print(largest(a))