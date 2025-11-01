class Node:
    def __init__(self,data,Next= None):
        self.data= data
        self.next= Next


arr = [0,1,2,3,4]
head = Node(arr[0])
mover = head
for i in range(1,len(arr)):
    temp = Node(arr[i])
    mover.next = temp
    mover = temp
    
temp = head
while(temp):
    print(temp.data,end = ' ->')
    temp = temp.next
print("null")