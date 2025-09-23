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
            


# def insertion(a):
#     print("Initial:", a)
#     for i in range(1, len(a)):
#         key = a[i]
#         j = i - 1
#         print(f"\n--- Outer loop i={i}, key={key} ---")
        
#         # shift elements
#         while j >= 0 and a[j] > key:
#             print(f"  Comparing key={key} with a[{j}]={a[j]} → shift")
#             a[j+1] = a[j]
#             print("  After shift:", a)
#             j -= 1
        
#         # insert key
#         a[j+1] = key
#         print(f"  Insert key={key} at position {j+1}")
#         print("  Array now:", a)
#     return a

# a = [9, 12, 14, 15, 6, 8, 13]
# print("\nFinal sorted:", insertion(a))
