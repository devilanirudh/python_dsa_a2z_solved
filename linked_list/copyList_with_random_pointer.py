"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return head
        hashset = {}
        temp = head
        while(temp!=None):
            hashset[temp]=Node(temp.val)
            temp = temp.next
        temp = head
        for k,v in hashset.items():
            v.next = hashset.get(k.next)
            v.random = hashset.get(k.random)
        return hashset[temp]

        