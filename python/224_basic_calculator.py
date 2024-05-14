# hard

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # convert to list
        stack = list(s.replace(' ', ''))
        return self.calculate_helper(stack)
    
    def calculate_helper(self, stack):
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        num = ''
        r = None
        eval = []
        bracket_num = 0
        while len(stack) > 0:
            # parse any-digit number
            while len(stack) > 0 and stack[-1] in numbers:
                v = stack.pop()
                num = v + num
            if num != '':
                # add back to stack as a number and reset num
                stack.append(int(num))
                num = ''
                continue
            if type(stack[-1]) == int:
                eval.append(stack.pop())
                continue
            if stack[-1] == '-':
                stack.pop()
                eval[-1] = eval[-1] * -1
                continue
            if stack[-1] == '+':
                stack.pop()
                continue
            if stack[-1] == ')':
                stack.pop()
                # pop everything
                exp = []
                bracket_num += 1
                while bracket_num > 0:
                    # handle internal brackets
                    if stack[-1] == ')':
                        bracket_num += 1
                    if stack[-1] == '(':
                        bracket_num -= 1
                    exp.insert(0, stack.pop())
                # remove the front bracket and evaluate
                result = self.calculate_helper(exp[1:])
                stack.append(result)
        return sum(eval)
