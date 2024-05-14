# medium

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l = s.split(" ")
        l = list(filter(lambda x: x != '', l))
        l.reverse()
        return " ".join(l)