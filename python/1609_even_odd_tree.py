# medium

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        queue.append((root, 0))
        
        prev_node_tuple = (TreeNode(0, None, None), -1)

        while len(queue) > 0:
            node_tuple = queue.pop(0)
            node = node_tuple[0]
            node_layer = node_tuple[1]

            # check if the node is correct polarity
            if node_layer % 2 == node.val % 2:
                return 'polarity'
            
            # check if node is correctly increasing or decreasing
            if prev_node_tuple[1] == node_layer:
                if node_layer % 2 == 0:
                    if node.val <= prev_node_tuple[0].val:
                        # need to strictly increase
                        return 'wat'
                else:
                    if node.val >= prev_node_tuple[0].val:
                        # need to strictly decrease
                        return 'no'
            
            # update prev_node_tuple
            prev_node_tuple = node_tuple

            # add new nodes to queue
            if node.left != None:
                queue.append((node.left, node_layer + 1))
            if node.right != None:
                queue.append((node.right, node_layer + 1))
        return True

def test():
    input = [1,10,4,3,None,7,9,12,8,6,None,None,2]
    root = TreeNode(input[0], None, None)
    i = 1
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if i >= len(input):
            continue
        left_node = None if input[i] == None else TreeNode(input[i], None, None)
        right_node = None if input[i + 1] == None else TreeNode(input[i + 1], None, None)
        node.left = left_node
        node.right = right_node
        if left_node != None:
            queue.append(left_node)
        if right_node != None:
            queue.append(right_node)
        i = i + 2

    s = Solution()
    return s.isEvenOddTree(root)
        
test()
