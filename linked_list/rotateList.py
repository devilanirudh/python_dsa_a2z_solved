# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:return head
        slow = head
        fast = head
        prev = slow
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        k = k % length
        if k == 0: return head
        for i in range(k):
            fast = fast.next
        
        while(fast.next!= None):
            prev = slow
            slow = slow.next
            fast = fast.next
        if slow.next == None:
            return head

        newhead = slow.next
        fast.next = head
        slow.next = None
        return newhead
        
        
        