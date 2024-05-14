# medium

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        p1 = 0
        p2 = 0
        
        def get_next(v, p):
            current_val = ""
            c = ""
            while p < len(v):
                c = v[p]
                if c == ".":
                    break
                current_val = current_val + c
                p = p + 1
            return (0, p + 1) if len(current_val) == 0 else (int(current_val), p + 1)
        
        while p1 < len(version1) or p2 < len(version2):
            i1, p1 = get_next(version1, p1)
            i2, p2 = get_next(version2, p2)

            if i1 < i2:
                return -1
            elif i1 > i2:
                return 1
        return 0
    
s = Solution()
print(s.compareVersion("1.01.234", "1.001.0.2"))