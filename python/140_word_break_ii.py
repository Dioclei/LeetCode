from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict_set = set(wordDict)
        return self.word_break_helper(s, word_dict_set)

    def word_break_helper(self, s, word_dict_set):
        if len(s) == 0:
            return []
        
        current_word = []
        sentences = []
        for i, c in enumerate(s):
            current_word.append(c)
            # check whether current_word is a word.
            current_word_string = ''.join(current_word)
            if current_word_string in word_dict_set:
                # sentence only contains this word
                if i == len(s) - 1:
                    sentences.append(current_word_string)
                # theres more to the sentence
                rest_of_sentence = self.word_break_helper(s[i+1:], word_dict_set)
                if len(rest_of_sentence) == 0:
                    # invalid sentence, discard word
                    continue
                # valid sentence(s)
                for rest in rest_of_sentence:
                    new_sentence = current_word_string + " " + rest
                    sentences.append(new_sentence)
        return sentences
                    
