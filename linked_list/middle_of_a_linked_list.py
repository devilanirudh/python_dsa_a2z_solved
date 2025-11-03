# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
                return temp
            temp = temp.next