# medium

class MinStack(object):
    """
    stack: list with enough space
    top_index: index of the topmost item in the stack
    minima: monotonic (strictly non-increasing) stack of local minima
        reasoning:
        1. invariant: the stack has multiple local minima, 
            1.1 note that we define the top of the stack to be a local minima as well.
        2. invariant: the minimum is the smallest local minima
        3. invariant: the next minimum is definitely before the current minimum because it is a stack

        hence we keep a monotonic (strictly non-increasing) stack of the local minima, so we will always know which value is the minimum.
    """

    def __init__(self):
        self.stack = []
        self.minima = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # add new value to stack
        self.stack.append(val)
        # if this value is smaller or equal to the current minimum, add it to the minima stack
        if len(self.minima) == 0 or val <= self.minima[-1]:
            self.minima.append(val)

    def pop(self):
        """
        :rtype: None
        """
        # what if the popped value is the minimum?
        
        if len(self.minima) != 0 and self.top() == self.minima[-1]:
            self.minima.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minima[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()