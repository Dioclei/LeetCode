# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            tail = self.traverse(root.left)
            tail.right = root.right
            root.right = root.left
            root.left = None
        

    def traverse(self, root):
        # traverse right side of root to get the tail
        if root.right:
            return self.traverse(root.right)
        else:
            return root

