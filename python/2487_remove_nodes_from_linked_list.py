# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # this is not the fastest solution because while it is O(n), it requires construction of tuple object.
        # actually no need to use helper function
        def helper(head):
            # returns the largest value and its corresponding node
            if head == None:
                return (None, None)
            largest_val, largest_node = helper(head.next)
            if largest_val == None:
                return (head.val, head)
            if head.val < largest_val:
                return (largest_val, largest_node)
            head.next = largest_node
            return (head.val, head)
        
        return helper(head)[1]


            

