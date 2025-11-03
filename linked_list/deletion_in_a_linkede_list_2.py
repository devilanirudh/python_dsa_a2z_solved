
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
        
def deletion_last(ll):
    temp =ll
    if temp is None or temp.next is None:return None
    while(temp.next.next!=None):
        temp = temp.next
    temp.next= None
    return ll

def deletion_first(ll):
    temp = ll
    if temp is None or temp.next is None:return ll
    ll = ll.next
    return ll      

def deletion_position(head,k):
    if head==None : return head
    if k ==1:
        temp = head
        head = head.next
        return head
    counter= 0
    temp = head
    previous = None
    while(temp!=None):
        counter+=1
        if(counter==k):
            previous.next=previous.next.next
            break
        previous = temp
        temp = temp.next
    return head

def deletion_value(head,el):
    if head == None:return head
    if head.data ==el:
        temp = head
        head = head.next
        return head
    previous = None
    temp = head
    while(temp!=None):
        if temp.data == el:
            previous.next = previous.next.next
            break
        previous = temp
        temp = temp.next
    return head


arr = [1,2,3,4,5]
lis = arr2ll(arr)
show(lis)
deletion_last(lis)
show(lis)
lis = deletion_first(lis)
show(lis)
lis = deletion_position(lis,3)
show(lis)
lis = deletion_value(lis,2)
show(lis)