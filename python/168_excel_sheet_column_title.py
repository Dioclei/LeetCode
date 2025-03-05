# Problem: Given a column number, convert it to an excel sheet column title, e.g. 1 = 'A', 2 = 'B', 26 = 'Z', 27 = 'AA', ...
# Intuition:
# - this can be thought of converting a base 10 number to a base 26 number (with A, B, C ...) as its digits
# - note that a baseX number ABC = A*X^2 + B*X^1 + C*X^0, so we can slowly construct the number

# Comments:
# - what tripped me up was that in a base 26 number, the digits should be [0, 1, 2, ... , 24, 25]
#   - but excel column number decided that 0 doesnt exist and is instead  [1, 2, 3, ... , 25, 26]
# - the math only works on 0 so there is a need to deduct 1 from the number when processing it

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        result = ""
        while num > 0:
            current_digit = chr(((num-1) % 26) + 65)
            num = (num-1) // 26
            result = current_digit + result
        return result
