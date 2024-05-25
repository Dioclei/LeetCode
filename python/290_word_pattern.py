# easy question in preparation for Word Pattern II (medium)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        parts = s.split(' ')
        if len(parts) != len(pattern):
            return False
        mapping = {}
        for index, character in enumerate(pattern):
            # character is mapped, check if it maps correctly
            if character in mapping: 
                if parts[index] != mapping[character]:
                    return False
                else:
                    continue
            # map new character, making sure that other characters don't have the same mapping (bijective)
            if parts[index] in mapping.values():
               return False
            mapping[character] = parts[index]
        return True
    
sol = Solution()
print(sol.wordPattern("abba", "cat dog dog cat"))

