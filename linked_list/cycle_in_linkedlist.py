# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:return False
        seen = set()
        temp = head
        while(temp):
            if temp in seen:return True
            seen.add(temp)
            if temp.next is None:return False
            temp = temp.next
        return False
        