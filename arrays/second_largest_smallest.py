def second_largest(a):
    largest = second_largest = float('-inf')
    for i in range(1,len(a)):
        if a[i]>largest:
            second_largest = largest
            largest = a[i]
        elif a[i]>second_largest and a[i]!=largest:
            second_largest = a[i]
    if largest == second_largest:
        return -1
    
    return second_largest

def second_smallest(a):
    smallest = second_smallest = float('inf')
    for i in range(1,len(a)):
        if a[i]<smallest:
            second_smallest = smallest
            smallest = a[i]
        elif a[i]<second_smallest and a[i]!=smallest:
            second_smallest = a[i]
    if smallest == second_smallest:
        return -1
    return second_smallest
    
a = [1,2,3,4,5,6]
print(second_largest(a))
print(second_smallest(a))

b = [6,5,4,3,2,1]
print(second_largest(b))
print(second_smallest(b))
    