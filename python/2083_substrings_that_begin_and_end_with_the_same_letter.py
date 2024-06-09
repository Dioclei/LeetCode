class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # keep a count of every letter that has been seen
        # for every past letter, a substring can be formed
        letters_seen = [0] * 26 # only lowercase letters
        count = 0
        for c in s:
            idx = ord(c) - 97
            # a substring can be formed with every past letter
            # a substring of length 1 can also be formed, hence add 1
            count = count + letters_seen[idx] + 1
            letters_seen[idx] += 1
        return count
