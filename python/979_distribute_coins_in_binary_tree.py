from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        steps, _ = self.distribute_helper(root)
        return steps
    def distribute_helper(self, root: Optional[TreeNode]) -> tuple[int, int]:
        '''
        helper returns 2 values:
        no. of steps to distribute for this whole subtree, plus bubbling excess/deficit -> int
        amount of excess/deficit, bubbled up to root -> int
        '''
        if root is None:
            # no need to redistribute to this node
            return (0, 0)
        # check subtrees
        # 1. if subtree has enough, assume it redistributes automatically (same algo but for subtree)
        # 2. one subtree deficit and one subtree excess, attempt to redistribute between them
        # 3. both subtrees deficit or excess
        l_steps, l_balance = self.distribute_helper(root.left)
        r_steps, r_balance = self.distribute_helper(root.right)
        parent_balance = root.val - 1
        new_balance = l_balance + r_balance + parent_balance
        # how many steps to balance things out, as much as possible?
        # if subtree is in deficit, i need to move coins down.
        # if subtree is in excess, i need to move coins up.
        # actual value doesn't matter because moving up and moving down consumes 1 step
        extra_steps = abs(l_balance) + abs(r_balance)
        return (extra_steps + l_steps + r_steps, new_balance)
    
    """
    After problem thoughts:
    The intuition for this problem is quite difficult to get, and 
    I only got it after writing out a few if statements and finally 
    realising the true, simple nature of the problem

    Basically, we want the coins to move as little as possible
    We don't know how many coins each node has, but we know the whole tree has exactly the number of coins we need
    So there are 2 invariants:
    1. if a subtree has a deficit, it must obtain more coins from its parent
    2. if a subtree has an excess, it must bubble coins up to its parent
    3. how the coins actually move doesnt matter, because by fulfilling 1 and 2, all nodes will have 1 coin at the end
    4. fulfilling 1 and 2 is optimal.
    The amount of coins each node has doesnt actually matter, only for calculating how much deficit/excess we have for each node
    """
