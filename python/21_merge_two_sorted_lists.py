# Linked List Problem!
# Note:
# - the linked lists are sorted, so all there is to do is to splice them together
# - the linked list can contain 0 items
# Intuition: 
# - linked list = recursion
# Algorithm:
# - because both lists are sorted, we are sure that the heads of each list is the smallest (respectively in each list)
# - take the smaller head
# - recursively sort and append to the tail

# Iterative:
# - note that it is possible to do this iteratively
# - using a while loop and comparing heads of each list,
# - remove heads until both lists are empty

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        # take the smaller head and return it with a sorted tail
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        