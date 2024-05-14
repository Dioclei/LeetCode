# medium

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """     
        
        def helper(head):
            if head == None:
                return head
            else:
                head.val = 2 * head.val
                head.next = helper(head.next)
                if head.next != None and head.next.val > 9:
                    head.val += 1
                    head.next.val = head.next.val % 10
                return head
            
        head = helper(head)
        if head.val > 9:
            head.val = head.val % 10
            head = ListNode(val=1, next=head)
        return head
        