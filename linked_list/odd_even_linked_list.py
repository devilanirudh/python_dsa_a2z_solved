# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next == None : return head
        first = head
        second_fix = head.next
        second = head.next
        while second and second.next:
            first.next = first.next.next
            first = first.next
            second.next = second.next.next
            second = second.next
        first.next = second_fix
        return head

        
        