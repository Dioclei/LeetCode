class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # need to append (a minimum number of characters) to s such that t becomes a substring of s
        # find maximum substring of t in s, then calculate the characters left
        p = 0
        for c in s:
            if p >= len(t):
                break
            curr = t[p]
            if c == curr:
                p += 1
        return len(t) - p