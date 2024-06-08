from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # preprocess, takes O(m), where m = number of items in dictionary
        dict_max_length = 0
        for word in dictionary:
            dict_max_length = max(dict_max_length, len(word))
        dictionary_set = set(dictionary)

        # O(n), where n = number of words in sentence,
        # counting helper, this is O(nk)
        sentence_list = sentence.split(" ")
        for i in range(len(sentence_list)):
            sentence_list[i] = self.replace_helper(dictionary_set, dict_max_length, sentence_list[i])
        
        # O(n)
        return " ".join(sentence_list)

    # dict_max_length can go up to 100
    # this is O(k), k <= 100
    def replace_helper(self, dict_set, dict_max_length, word):
        for i in range(dict_max_length):
            word_slice = word[:i+1]
            if word_slice in dict_set:
                return word_slice
        return word
    
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
sol = Solution()
print(sol.replaceWords(dictionary, sentence))