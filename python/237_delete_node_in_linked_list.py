# medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # linked list should look like this:
        # (some nodes) -> (given node) -> (at least one node)
        
        # O(1)
        # make given node's value the next node's value 
        # (i.e. make given node an exact copy of the next node)
        # then set tail of given node to the next node's tail

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next