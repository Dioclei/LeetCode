# Problem: check if a tree has its subtrees mirrored
# Intuition:
# - if i can flip one of the subtrees, it is easier to check if the subtrees are the same
# - i will traverse the subtrees with a queue (bfs) and flip one of the subtrees by adding in the nodes in a flipped order
# - checking the trees similarity is the same algorithm as in 100 Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []
        queue.append((root.left, root.right))
        while queue:
            curr = queue.pop(0)
            if curr[0] == None and curr[1] == None:
                continue
            if curr[0] == None or curr[1] == None:
                return False
            if curr[0].val != curr[1].val:
                return False
            queue.append((curr[0].left, curr[1].right))
            queue.append((curr[0].right, curr[1].left))
        return True

            
        