# Objective is to look for the longest common prefix between strings
# Wrong intuition: I initially thought it was 2 strings and wanted to use a two-pointer solution
# In fact I only need 1 pointer to check any number of strings

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = 0
        min_len = len(strs[0]) # minimum length of all strings
        for s in strs:
            min_len = min(min_len, len(s))
        # check that all strings have the same character at the same position to find the prefix
        while p < min_len:
            same_character = True
            for s in strs:
                if s[p] == strs[0][p]:
                    continue
                else:
                    same_character = False
                    break
            if same_character:
                p += 1
            else:
                break

        # slice the common prefix and return it
        return strs[0][:p]