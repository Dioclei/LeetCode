# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1, l2, carry):
            if l1 is None and l2 is None:
                return ListNode(1) if carry == 1 else None
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            l1_next = None if l1 is None else l1.next
            l2_next = None if l2 is None else l2.next
            
            val = l1_val + l2_val + carry
            if val > 9:
                val = val % 10
                return ListNode(val, helper(l1_next, l2_next, 1))
            else:
                return ListNode(val, helper(l1_next, l2_next, 0))
        return helper(l1, l2, 0)