class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1):
            c1 = s[i]
            c2 = s[i + 1]
            diff = abs(ord(c1) - ord(c2))
            if diff == 32:
                s = s[:i] + s[i+2:]
                return self.makeGood(s)
        return s

