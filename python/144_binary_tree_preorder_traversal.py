# Problem: construct a preorder traversal of a binary tree
# Intuition:
# - i will do it iteratively because recursive solution is trivial
# - preorder = print root first, then print left, then print right
# - important to track the root node, we will use a stack to do so

# Comments
# - Can make comparison with 94 to see the differences between inorder and preorder
# - Understand that for inorder you need to travel to the leftmost node first, whereas for preorder it's travel to the root first

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left) # visit left first so we append left last
        return result
