# Objective is to check whether a sequence is valid. Every open parentheses must have a corresponding closed parenthesis, in order.
# Intuition when I see parenthesis, I think of a stack. But it is key to think why this is actually the case.
# A stack keeps track of a sequence and reveals the topmost item.
# It is suitable because we want to close the most recent not-closed open bracket. It is easy to remove all the closed open brackets by popping them off the stack.

# Another reason why it is suitable is because we want to resolve the most recent sub-problem.

class Solution:
    def closes(self, c1, c2):
        return (c1 == "(" and c2 == ")") or (c1 == "[" and c2 == "]") or (c1 == "{" and c2 == "}")

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif self.closes(stack[-1], c):
                # pop it off the stack
                stack.pop()
            else:
                # add it to the stack
                stack.append(c)
        # for the string to be valid, the stack has to have nothing left
        return len(stack) == 0

