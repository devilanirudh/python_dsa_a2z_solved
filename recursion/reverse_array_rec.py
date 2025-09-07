def arr_rec(a):
    if(len(a)==0):
        return
    b = a[0]
    a.pop(0)
    arr_rec(a)
    a.append(b)
    return a

print(arr_rec([1,2,3,4,5]))