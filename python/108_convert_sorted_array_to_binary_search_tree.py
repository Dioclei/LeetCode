# Problem: convert a sorted array into a binary search tree
# Intuition: 
# - the root node of the bst is always the midpoint of the sorted array.
# - we can recursively construct the bst by partitioning the array

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive approach
# should be faster and more memory efficient to use a helper function that takes in list boundary pointers instead of creating a new partitioned list every time
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        # take the midpoint and create a root node
        mid_idx = len(nums) // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        # make sure no out of bounds
        if mid_idx + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root

