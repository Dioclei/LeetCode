# easy

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        p1 = 0
        p2 = len(s) - 1
        vowels = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        sl = list(s)
        while p1 < p2:
            if sl[p1] in vowels and sl[p2] in vowels:
                t = sl[p1]
                sl[p1] = sl[p2]
                sl[p2] = t
                p1 += 1
                p2 -= 1
            elif s[p1] not in vowels:
                p1 += 1
            else:
                p2 -= 1
        return "".join(sl)