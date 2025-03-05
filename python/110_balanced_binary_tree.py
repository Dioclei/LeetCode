# Problem: find out whether a tree is height-balanced
# Intuition:
# - if a tree is height-balanced, then all its nodes' subtrees never differ by a height of more than 1
# - calculate the height of each node, starting from the leaves, and make sure that every node is height-balanced.
# - this bottom up approach ensures we don't need to call height for the same node again as opposed to a top-down approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeightAndCheckBalance(self, node):
        if node == None:
            return 0, True
        left_height, left_balanced = self.getHeightAndCheckBalance(node.left)
        if not left_balanced:
            return 0, False # end early
        right_height, right_balanced = self.getHeightAndCheckBalance(node.right)
        if not right_balanced:
            return 0, False # end early
        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, is_balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, is_balanced = self.getHeightAndCheckBalance(root)
        return is_balanced

        