# easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None or head.next == None:
            return False
        
        tortoise = head
        hare = head.next

        while tortoise != hare:
            if hare.next == None or hare.next.next == None:
                return False
            if tortoise.next == None:
                return False
            hare = hare.next.next
            tortoise = tortoise.next
        return True
