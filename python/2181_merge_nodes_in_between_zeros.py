from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        if head.next == None:
            return None
        head = head.next
        while head.val != 0:
            sum += head.val
            head = head.next
        return ListNode(sum, self.mergeNodes(head))
