# A similar problem to 66, involves string traversal
# Intuition
# - brute force, but is there a better way?

# Comments
# - yes, better to use bit manipulation
# - sounds difficult but it's actually very simple.
# - calculate the sum without carry using XOR
# - calculate the carry using AND and SHIFT LEFT (because 1 AND 1 give a carry)
# - now do anther addBinary call to add without-carry and carry together.
# - this will recursively work until carry == 0

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # we will operate on the longer binary string
        if len(a) < len(b):
            temp = a
            a = b
            b = temp
        new_bin = []
        i = len(a) - 1
        diff = len(a) - len(b)
        carry = 0
        while i >= 0:
            if i-diff < 0:
                val = int(a[i]) + carry
            else:
                val = int(a[i]) + int(b[i-diff]) + carry
            if val == 3:
                carry = 1
                new_bin.insert(0, "1")
            elif val == 2:
                carry = 1
                new_bin.insert(0, "0")
            elif val == 1:
                carry = 0
                new_bin.insert(0, "1")
            else:
                carry = 0
                new_bin.insert(0, "0")
            i -= 1
        if carry:
            new_bin.insert(0, "1")
        return "".join(new_bin)
