# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        if k <= 1 or not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the k-th node from group_prev (inclusive of next)
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes left -> done

            group_next = kth.next  # node after the k-group

            # Reverse the k nodes in-place:
            prev = group_next
            curr = group_prev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # After reversing:
            # prev is the new head of this reversed group
            # group_prev.next was the original head (now tail)
            tail = group_prev.next
            group_prev.next = prev
            group_prev = tail  # move group_prev to tail for next iteration

