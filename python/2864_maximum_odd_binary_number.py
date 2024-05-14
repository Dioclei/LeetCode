# easy

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = 0
        for x in s:
            if x == '1':
                ones += 1
        return '1' * (ones - 1) + '0' * (len(s) - ones) + '1'