def uniona(a, b):
    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return list(set(c))

a = [1, 2, 3]
b = [4, 5,5]
print(uniona(a, b))
