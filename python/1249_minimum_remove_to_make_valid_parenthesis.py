# medium

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = 0
        to_remove = set()
        for i in range(len(s)):
            c = s[i]
            if c == ")":
                count -= 1
                if count < 0:
                    count += 1
                    to_remove.add(i)
            elif c == "(":
                count += 1
        j = len(s) - 1
        while count > 0:
            # remove all "(" starting from the back
            c = s[j]
            if c == "(":
                to_remove.add(j)
                count -= 1
            j -= 1
        arr = []
        for i in range(len(s)):
            if not i in to_remove:
                arr.append(s[i])
        res = "".join(arr)
        return res
    
def test():
    s = Solution()
    r = s.minRemoveToMakeValid("(((()))))")
    print(r)

test()
            
                    
