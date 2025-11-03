class ListNode:
    def __init__(self,val=0,next=None):
        self.val= val
        self.next = next

def arr2ll(a):
    head = ListNode(a[0])
    mover = head
    for i in range(1,len(a)):
        temp = ListNode(a[i])
        mover.next = temp
        mover = temp
    return head

def show(head):
    temp = head
    while(temp):
        print(temp.val,end =' -> ')
        temp = temp.next
    print(None)


def insert_head(head,v):
    temp = ListNode(v,head)
    return temp

def middle(head):
    counter=0
    temp = head
    while(temp!=None):
        counter+=1
        temp = temp.next
    counter = (counter//2)+1
    k = 0
    temp = head
    while(temp!=None):
        k+=1
        if k==counter:
            return temp.val
        temp = temp.next

a = [1,2,3,4,5,6]
ll = arr2ll(a)
show(ll)
print(middle(ll))
# ll = insert_head(ll,10)
# show(ll)