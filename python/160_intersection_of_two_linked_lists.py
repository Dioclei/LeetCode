# Problem: Given a linked list that may or may not have 2 heads, find the intersection
# Intuition:
# - the end of the linked list must be equal if there is an intersection
# - compare the two ends of the linked list using a stack
# - this will be O(m+n) time complexity with O(m+n) space complexity
#   - doesn't achieve O(1) space complexity, i will study the answer for that

# Comments
# - no need to use 2 stacks, simply keeping a hashmap of one linked list's nodes will be enough
# - that will be O(m) space complexity
# - for O(1) space complexity, we simply start comparing the nodes at the first possible point that they intersect.
# - to do so, we need the length of the linked lists,
#   - for instance if A is 5 nodes and B is 7 nodes, then we have 2 pointers starting at A[0] and B[2]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        stackA = []
        currA = headA
        while currA:
            stackA.append(currA)
            currA = currA.next
        stackB = []
        currB = headB
        while currB:
            stackB.append(currB)
            currB = currB.next
        intersection = None
        while stackA and stackB:
            a = stackA.pop()
            b = stackB.pop()
            if a is b:
                intersection = a
            else:
                break
        return intersection

