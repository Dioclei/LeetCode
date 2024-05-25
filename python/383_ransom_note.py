class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = [0 for i in range(26)]
        # index all letters in magazine
        for c in magazine:
            idx = ord(c) - 97
            letter_count[idx] += 1
        # test ransomNote against letter_count
        for c in ransomNote:
            idx = ord(c) - 97
            letter_count[idx] -= 1
            if letter_count[idx] < 0:
                return False
        return True