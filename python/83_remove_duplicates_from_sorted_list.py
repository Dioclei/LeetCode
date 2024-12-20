# Linked list question, remove dupes in a sorted linked list
# Intuition
# - it is easy to remove a node in a linked list
# - the problem can be broken down into subproblems - we can always run the algorithm on a later section of the linked list
# - remove the head, and not the next node, so that we can check for dupes again with the next node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            # dupe exists, remove the head and continue deleting dupes
            return self.deleteDuplicates(head.next)
        else:
            # no dupe, don't remove the head and continue deleting dupes
            head.next = self.deleteDuplicates(head.next)
            return head
        