def selection(a):
    length = len(a)
    for i in range(length-1):
        min_idx = i
        for j in range(i+1,length):
            if a[j]<a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [2,4,1,9,5]
print(selection(a))