class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordList = sentence.split(' ')
        for i, word in enumerate(wordList):
            if word.startswith(searchWord):
                return i + 1
        return -1