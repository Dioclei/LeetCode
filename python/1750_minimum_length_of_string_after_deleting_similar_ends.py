# medium

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        p1 = 0
        p2 = l - 1
        if l == 1:
            return l
        if s[p1] != s[p2]:
            return l
        while p1 < p2:
            if s[p1 + 1] == s[p1]:
                # new left character is same as current left character
                p1 = p1 + 1
            elif s[p2 - 1] == s[p2]:
                # new right character is same as current right character
                p2 = p2 - 1
            elif s[p1 + 1] == s[p2 - 1]:
                # new left character is the same as new right character
                p1 = p1 + 1
                p2 = p2 - 1
                if p1 == p2:
                    return 1
            else:
                return p2 - p1 + 1 - 2
        else: return 0

    def test(self):
        return self.minimumLength("bbbbbbbacbb")
