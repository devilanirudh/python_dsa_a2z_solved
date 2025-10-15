def leaders(a):
    maxi = float('-inf')
    leaders = []
    for i in range(len(a)-1,-1,-1):
        if a[i]>maxi:
            maxi = a[i]
            leaders.append(a[i])
    return leaders
            
    

a = [10,22,12,3,0,6]
print(leaders(a))