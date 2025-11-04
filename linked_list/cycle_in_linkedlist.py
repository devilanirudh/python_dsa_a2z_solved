# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def arr2ll(arr):
    head = ListNode(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        mover.next = temp
        mover = temp
    return head

def show(ll):
    temp = ll
    while(temp):
        print(temp.data,end = ' -> ')
        temp=temp.next
    print("null")

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:return False
        arr=[]
        i=0
        temp = head
        while(i<10^4):
            if temp in arr:return True
            arr.append(temp)
            temp = head.next
            i+=1
        return False


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head==None or head.next==None:return False
#         seen = set()
#         temp = head
#         while(temp):
#             if temp in seen:return True
#             seen.add(temp)
#             if temp.next is None:return False
#             temp = temp.next
#         return False

# tORTOISE AD THE Hare Algorithm

def tortoise_and_hare_cycle(head):
    if head is None or head.next is None:return False
    slow = head
    fast = head
    while(fast!=None and fast.next!=None):
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False


      
head = [3,2,0,-4]
lis = arr2ll(head)        
print(Solution().hasCycle(lis))