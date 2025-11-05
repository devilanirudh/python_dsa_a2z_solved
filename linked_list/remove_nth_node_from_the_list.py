# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None :return None
        if head.next == None: 
            head = None
            return head 
        temp = head
        nu_ch = head
        while(temp!=None and temp.next!=None):
            nu_ch = temp
            for i in range(n):
                if nu_ch is None:
                    break
                nu_ch = nu_ch.next
            if nu_ch is None:
                break
            if nu_ch.next == None:
                temp.next=temp.next.next
                return head
            temp = temp.next
        nu_ch = head
        for i in range(n):
            if nu_ch is None:
                break
            nu_ch = nu_ch.next
        if nu_ch is None:
            head = head.next
        
        return head
                    
        