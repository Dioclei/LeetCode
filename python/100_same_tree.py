# Problem: check if two trees are identical structurally and value-wise
# Intuition
# - a node is equal if it has the same value and the same children
# - recursively check if the nodes are equal

# Comments
# - previously, i tried to use a inorder traversal to check whether the trees are the same
# - however, inorder (or any other order) traversal may be the same for different trees, so it doesn't work
# - what really matters in this problem is to stepwise traverse the tree in the same manner and check the value at each step.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# iterative attempt
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use a queue and do bfs to traverse through the tree
        p_queue = [p]
        q_queue = [q]
        while p_queue and q_queue:
            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)
            if p_curr == None and q_curr == None:
                continue
            if p_curr == None or q_curr == None:
                return False
            if p_curr.val != q_curr.val:
                return False
            p_queue.append(p_curr.left)
            p_queue.append(p_curr.right)
            q_queue.append(q_curr.left)
            q_queue.append(q_curr.right)
        return True