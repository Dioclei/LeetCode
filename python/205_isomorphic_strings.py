class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMapping = {}
        tMapping = {}
        for i in range(len(s)):
            x = s[i]
            # search for x in sMapping
            if x in sMapping:
                y = t[i]
                z = sMapping[x]
                if y != z:
                    return False
            else:
                # add x to sMapping and corresponding character to tMapping
                y = t[i]
                if y in tMapping:
                    return False
                else:
                    sMapping[x] = y
                    tMapping[y] = x
        return True


        
