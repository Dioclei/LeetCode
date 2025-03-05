# Problem: find out if any one of the root-to-leaf paths have a sum of values equal to targetSum
# Intuition:
# - need to at least traverse from root to leaf, and traverse the complete tree to find out if there are no such sums
# - possible to reduce calculations by caching the cumulative sum at each node
# - use a dfs to traverse the tree, and store the current sum
# - dfs can be implemented iteratively with a stack, and current sum data can be stored with the stack
# Comments
# - this algorithm can also be implemented recursively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        stack = []
        stack.append((root.val, root)) # (current_sum, node)
        while stack:
            current_sum, node = stack.pop()
            if not node.left and not node.right:
                # check if the sum is equal
                if current_sum == targetSum:
                    return True
            if node.left:
                stack.append((current_sum + node.left.val, node.left))
            if node.right:
                stack.append((current_sum + node.right.val, node.right))
        return False
