# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None : return head
        import heapq
        max_heap = []
        temp = head
        while(temp!=None):
            heapq.heappush(max_heap,(temp.val))
            temp = temp.next
        temp = head
        while(max_heap):
            a = heapq.heappop(max_heap)
            temp.val = a
            temp = temp.next
        return head


#approach 2 without extra space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:return head
        def middle(head):
            slow = head
            fast = head.next
            while(fast!=None and fast.next!=None):
                slow = slow.next
                fast = fast.next.next
            return slow
        def merge2(left,right):
            dummy = ListNode(-1)
            temp = dummy
            while(left and right):
                if (left.val<right.val):
                    temp.next  = left
                    temp = left
                    left = left.next
                else:
                    temp.next = right
                    temp = right
                    right = right.next
            if(left):temp.next = left
            if right:temp.next = right
            return dummy.next
                
        mid = middle(head)
        left_head = head
        right_head = mid.next
        mid.next = None
        left_head = Solution().sortList(left_head)
        right_head = Solution().sortList(right_head)
        return merge2(left_head,right_head)




        
        


        
        