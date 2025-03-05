# Problem: find the maximum depth of a binary tree
# Intuition:
# - traverse through the tree and keep track of the depth
# - iteratively, this can be done with a dfs (queue) or bfs (stack) 
# - recursively, this can be done by calling the same method again on the subtrees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recursive approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        max_subtree_depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 1 + max_subtree_depth

# iterative approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # using a queue
        queue = []
        queue.append((1, root))
        max_depth = 0
        while queue:
            curr = queue.pop(0)
            max_depth = max(max_depth, curr[0])
            if curr[1].left:
                queue.append((curr[0] + 1, curr[1].left))
            if curr[1].right:
                queue.append((curr[0] + 1, curr[1].right))
        return max_depth

        