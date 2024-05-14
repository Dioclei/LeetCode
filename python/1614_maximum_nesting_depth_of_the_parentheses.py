class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        c = 0
        m = 0
        for x in s:
            if x == "(":
                c += 1
                m = max(m, c)
            elif x == ")":
                c -= 1
        # if c > 0, there is extra "("
        if c > 0:
            m = m - c
        return m

def test():
    s = Solution()
    res = s.maxDepth("(1+(2*3)+((8)/4))+1")
    print(res)

test()