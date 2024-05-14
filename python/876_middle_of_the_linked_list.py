# easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 1
        node = head
        while node.next != None:
            node = node.next
            count += 1
        dist_to_middle = count // 2
        node = head
        while dist_to_middle > 0:
            node = node.next
            dist_to_middle -= 1
        return node