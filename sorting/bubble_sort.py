def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [13,24,16,20,9,52]
print(bubble(a))
            