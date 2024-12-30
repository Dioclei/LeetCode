# Problem: Convert an excel sheet column number, e.g. "AA" to its numerical value e.g. "27"
# Intuition
# - the excel sheet column number is basically a number in base 26: A = 1, B = 2, ... Z = 26
# - we can easily convert a number from base 26 to base 10 by doing math in the form of 26^X * Y 
# - e.g. "BB" = 26^1 * 2 + 26^0 * 2

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = len(columnTitle) - 1
        num = 0
        for c in columnTitle:
            digit_value = ord(c) - ord("A") + 1
            num = num + 26 ** power * digit_value
            power -= 1
        return num