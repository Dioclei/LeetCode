# Problem: find the minimum depth of a binary tree
# Intuition:
# - the minimum depth of a binary tree is the length of the shortest path from the root node to a leaf node
# - no need to traverse the tree fully, better to traverse the tree level by level
# - bfs is most well suited for this task
# - use bfs to find the nearest leaf to the root
# - to implement bfs, we will use a queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = []
        queue.append((1, root))
        while queue:
            dist, node = queue.pop(0)
            if not node.left and not node.right:
                return dist # cut the loop at the first leaf node found. because this is a bfs, we guarantee that it is the nearest leaf node.
            if node.left:
                queue.append((dist + 1, node.left))
            if node.right:
                queue.append((dist + 1, node.right))
            

        