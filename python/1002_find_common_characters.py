from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # do iteratively with O(1) memory
        current_count = self.character_count(words[0])
        for word in words[1:]:
            current_count = self.take_intersection(current_count, self.character_count(word))
        # translate to character list
        characters = []
        for index, count in enumerate(current_count):
            character = chr(index + 97)
            for i in range(count):
                characters.append(character)
        return characters
    
    def character_count(self, word):
        # returns a 26 length array with the count of each characters
        count = [0 for i in range(26)]
        for c in word:
            idx = ord(c) - 97
            count[idx] += 1
        return count

    def take_intersection(self, count1, count2):
        # for each letter in countx, take the minimum count
        count = [0 for i in range(26)]
        for i in range(26):
            m = min(count1[i], count2[i])
            count[i] = m
        return count

