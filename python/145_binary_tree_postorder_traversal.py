# Problem: construct a postorder traversal from a binary tree
# Intuition:
# - print left and right nodes first before printing the root

# Comments
# - recursive solution is trivial
# - iterative algorithm is very similar to 94 (inorder):
# - travel to leftmost node, and process the node
#   - if there is no unprocessed right node (additional condition for postorder)
#   - hence need to keep track of previous node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution, very intuitive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left, right = [], []
        if root.left:
            left = self.postorderTraversal(root.left)
        if root.right:
            right = self.postorderTraversal(root.right)
        return left + right + [root.val]
            
# iterative approach (1 stack)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = []
        curr = root
        prev = None
        while stack or curr:
            # move to the leftmost node and add the chain of left nodes to the tree
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                # do we process the topmost item?
                curr = stack[-1]
                # check whether it has an unprocessed right node
                # guarantee: the first node to be processed is the leftmost leaf node that doesn't have children
                if not curr.right or curr.right == prev:
                    # process node
                    stack.pop()
                    result.append(curr.val)
                    prev = curr
                    curr = None
                # if there is a right node, move to the right node (and restart appending the leftest nodes again)
                else:
                    curr = curr.right
        return result


            
            
