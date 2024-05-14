def evaluate_math_expression(math_expression) -> float:
    stack = []
    for x in math_expression:
        if x == ')':
            # do some popping
            p = stack.pop() # is whatever before ')'
            new_exp = []
            while (p != '('):
                new_exp = [p] + new_exp
                p = stack.pop()
            # p is a '(' right now and has been popped
            # evaluate the new_exp
            output = evaluate_math_expression(new_exp)
            stack.append(output) # append as an int
        else:
            stack.append(x)

    # no more brackets in the expression
    return evaluate(stack)

def evaluate(ll) -> float:
    if len(ll) == 1:
        return float(ll[0])
    else:
        # check what the next operand is
        operand = ll[1]
        if operand == '+':
            return float(ll[0]) + evaluate(ll[2:])
        elif operand == '-':
            return float(ll[0]) - evaluate(ll[2:])
        elif operand == '*':
            # do the operation first
            num = float(ll[0]) * float(ll[2])
            if len(ll) > 3:
                new_ll = [num] + ll[3:]
                return evaluate(new_ll)
            else: return num
        else:
            # operand = '/'
            num = float(ll[0]) / float(ll[2])
            if len(ll) > 3:
                new_ll = [num] + ll[3:]
                return evaluate(new_ll)
            else: return num

def test():
    string = '2/(4/7*6/9-7)/(2/4*(1-3))'
    print(evaluate_math_expression(string))

test()
    