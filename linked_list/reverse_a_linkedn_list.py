class ll:
    def __init__(self,data,Next = None):
        self.data=data
        self.next= Next


def arr2ll(arr):
    head = ll(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = ll(arr[i])
        mover.next = temp
        mover = temp
    return head

def show(ll):
    temp = ll
    while(temp):
        print(temp.data,end = ' -> ')
        temp=temp.next
    print("null")

def reverse(head):
    temp = head
    stack = []
    while(temp!=None):
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while(temp!=None):
        temp.data =  stack[-1]
        stack.pop()
        temp = temp.next
    return head

def reverse_ll_nospace(head):
    temp = head
    prev=None
    while(temp!=None):
        front = temp.next
        temp.next=prev
        prev = temp
        temp = front
    return prev



arr = [1,2,3,4,5]
lis = arr2ll(arr)
show(lis)
# lis = reverse(lis)
# show(lis)
lis = reverse_ll_nospace(lis)
show(lis)