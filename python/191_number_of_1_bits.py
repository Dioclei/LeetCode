# Problem: Given a positive integer, find the number of set bits (1) in its binary representation
# Intuition:
# - check the bit at each position using bit masks and check if it is a 1
# - total up the number of 1 bits
# - i know that the constraint is <= 2^31 - 1 so the number will not be more than 32 bits long

# Comments
# - approach works and is good
# - alternative: there is a trick to flip the least significant 1 bit to 0, by simply doing n & (n-1)
#   - using this trick, we can do the operation until n becomes 0

class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        mask = 1
        for i in range(32):
            if mask & n == mask:
                weight += 1
            mask = mask << 1
        return weight
