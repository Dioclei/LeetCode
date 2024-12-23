# Problem: travel a binary tree inorder
# Intuition
# - inorder means to travel the left nodes, then the root, then the right nodes
# - recursively travel in a dfs manner

# Comments
# - recursive approach works
# - possible to do iterative approach with a stack instead
# - notice that we can implement a dfs with a stack too
# - note that inorder is not exactly a dfs because in a dfs the root node is travelled first before left side is travelled.
# - a traversal more similar to dfs is preorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

# iterative approach attempt
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = []
        curr = root
        while curr or stack:
            # we traverse the tree with the help of the stack.
            # keep track of all the leftmost nodes so we can always backtrack to it eventually to process the right side
            # the actual node we are processing is the one indicated by the curr pointer, not the top of the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            # no more left node, we log the value and process the most recent node and its right side
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right # move on to process right side
        return res

# iterative approach attempt (wrong attempt)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            curr = stack[-1]
            # this is wrong, we don't want the stack to tell us where the next node is
            # this will result in an infinite loop, because we will end up popping a left node and adding it back again
            if curr.left:
                stack.append(curr.left)
            else:
                res.append(curr.val)
                stack.pop()
                if curr.right:
                    stack.append(curr.right)
        return res


            


        