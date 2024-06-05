from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count letters in palindrome
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        has_odd = False
        palindrome_length = 0
        for c in counter:
            # add to palindrome as much as possible
            if counter[c] % 2 == 0:
                palindrome_length += counter[c]
            else:
                palindrome_length += counter[c] - 1
                has_odd = True
        if has_odd:
            palindrome_length += 1
        return palindrome_length