def partition(a,low,high):
    pivot = a[low]
    i = low+1
    j = high
    while True:
        while i<=j and a[i]<=pivot:
            i= i+1
        while i<=j and a[j]>=pivot:
            j = j-1
        if i <= j:
            a[i],a[j] = a[j],a[i]
        else:
            break
    a[low],a[j] = a[j],a[low]
    return j
            


def quick_sort(a,low,high):
    if low<high:
        p = partition(a,low,high)
        quick_sort(a,low,p-1)
        quick_sort(a,p+1,high)
    return a 


a = [1,5,92,4,0]
print(quick_sort(a,0,len(a)-1))