class Solution:
    def next(self, c: str):
        # a = 97 to z = 122
        new_val = (ord(c) - 97 + 1) % 26 + 97
        return chr(new_val)

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # basically for this problem, we need to check if str2 is a subsequence of a modified str1
        # we know that each character of str1 can either:
        # 1. stay the same
        # 2. change to the next character, cyclically, so a -> b, b -> c, ..., z -> a
        # so the idea is to check for subsequence but keep the possibilities in mind
        pStr1 = 0
        pStr2 = 0
        while pStr1 < len(str1) and pStr2 < len(str2):
            # match current character
            if str1[pStr1] == str2[pStr2] or self.next(str1[pStr1]) == str2[pStr2]:
                # is a match
                # check if str2 is fully matched (subsequence has been found)
                if pStr2 == len(str2) - 1:
                    return True
                # match next character in str2
                pStr1 += 1
                pStr2 += 1
            else:
                # is not a match
                # try to find another character to match in str1
                pStr1 += 1
        return False
    
s = Solution()
str1 = "abc"
str2 = "ad"
s.canMakeSubsequence(str1, str2)

            




    
