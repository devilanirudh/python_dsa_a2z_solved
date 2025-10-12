def longest_subarray(n,k):
    hash_map = {}
    prefix_sum = 0
    length = 0
    for i in range(len(n)):
        prefix_sum = n[i]+prefix_sum
        if k == prefix_sum:
            length = i+1
        to_check=prefix_sum-k
        if to_check in hash_map:
            f = hash_map.get(to_check)
            l = i-f
            if length < l:
                length = l
        if prefix_sum not in hash_map:
            hash_map.update({prefix_sum:i})
        if k == prefix_sum:
            length = i+1
    return length


n= [1,2,0,0,0,0,0,3,1,1,1,1,4,2,3] 
k=3
print(longest_subarray(n,k))