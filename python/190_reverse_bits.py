# Problem: reverse the bits of a 32 bit unsigned integer
# Intuition:
# - convert the integer to a binary string and perform a reverse operation on the string, and convert back

# Comments
# - I didn't know how to manipulate bits even though I knew of the bit shift and bit mask operators
# - Can try using bit operators to achieve what I want instead for binary numbers

# string manipulation approach (not preferred)
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:]
        # pad the string to 32 width
        binary_string = binary_string.zfill(32)
        # convert to list for processing
        binary_string = list(binary_string)
        i = 0
        while i < len(binary_string) / 2:
            j = len(binary_string) - 1 - i
            temp = binary_string[i]
            binary_string[i] = binary_string[j]
            binary_string[j] = temp
            i += 1
        result = int("".join(binary_string), base=2)
        return result

# bit manipulation approach with a loop
class Solution:
    def reverseBits(sef, n: int) -> int:
        # since it is a 32 bit number, we will iterate through each bit and reverse it
        mask = 1
        result = 0
        for i in range(32):
            bit = mask & n
            bit = bit >> i << (31 - i)
            result = bit | result
            mask = mask << 1
        return result

# bit manipulation approach with a loop provided by leetcode editorial
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

# bit manipulation approach without loop
# this requires 2 opposite masks, then swapping the values, from 16 bits to 8 to 4 to 2 to 1
class Solution:
    def reverseBits(self, n: int) -> int:
        # 16 bit swap
        n = (0xFFFF0000 & n) >> 16 | (0x0000FFFF & n) << 16
        # 8 bit swap
        n = (0xFF00FF00 & n) >> 8 | (0x00FF00FF & n) << 8
        # 4 bit swap
        n = (0xF0F0F0F0 & n) >> 4 | (0x0F0F0F0F & n) << 4
        # 2 bit swap
        n = (0xCCCCCCCC & n) >> 2 | (0x33333333 & n) << 2
        # 1 bit swap
        n = (0xAAAAAAAA & n) >> 1 | (0x55555555 & n) << 1
        return n