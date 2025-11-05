# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp = head
        if head is None : return False
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        i = 0 
        j = len(arr)-1
        while(i<=j):
            if arr[i]!=arr[j]:return False
            i+=1
            j-=1
        return True


 # o(1) ssolution
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None :return True
        def middle(head):
            slow = head
            fast = head
            while(fast.next!=None and fast.next.next!=None):
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse(slow):
            temp = slow.next
            prev = None
            while(temp!=None):
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev
        def palin(head,prev):
            temp = head
            temp1 = prev
            while(temp1!=None and temp!= None):
                if temp1.val!=temp.val:
                    reverse(prev)
                    return False
                temp1 = temp1.next
                temp = temp.next
            reverse(prev)
            return True
        x = middle(head)
        pr = reverse(x)
        return palin(head,pr)

        




                