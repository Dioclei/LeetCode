class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = list(s)
        is_word = False
        count = 0

        for i in range(len(l) - 1, -1, -1):
            c = l[i]
            if is_word and c == " ":
                break
            elif not is_word and c != " ":
                is_word = True
                count += 1
            elif c != " ":
                count += 1
        
        return count

def test01():
    s = Solution()
    print(s.lengthOfLastWord("a"))

test01()