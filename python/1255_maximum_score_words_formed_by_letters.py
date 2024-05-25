from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # calculate score of each word
        word_scores = [0 for i in words]
        for index, word in enumerate(words):
            word_score = 0
            for letter in word:
                idx = ord(letter) - 97
                word_score += score[idx]
            word_scores[index] = word_score
        # index letters
        letters_map = [0 for i in range(26)]
        for letter in letters:
            idx = ord(letter) - 97
            letters_map[idx] += 1
        traversals = [[i] for i in range(len(words))]
        max_score = 0
        for t in traversals:
            max_score = max(max_score, self.traverse(t, words, word_scores, letters_map))
        return max_score
        
    def traverse(self, chosen_idx, words, word_scores, letters_map):
        # check if chosen_words fulfil the letters requirement
        letters_map_copy = letters_map.copy()
        total_score = 0
        for index in chosen_idx:
            word = words[index]
            for letter in word:
                idx = ord(letter) - 97
                letters_map_copy[idx] -= 1
                if letters_map_copy[idx] < 0:
                    # too many words!
                    return 0
            # enough letters!
            # count score
            word_score = word_scores[index]
            total_score += word_score
        # try to add more words
        for new_chosen_idx in self.choose_new_words(chosen_idx, words):
            total_score = max(total_score, self.traverse(new_chosen_idx, words, word_scores, letters_map))
        return total_score
    
    def choose_new_words(self, chosen_idx, words):
        # based on current list of chosen words, return a new list
        new_ways = []
        last_i = chosen_idx[-1]
        for i in range(last_i + 1, len(words)):
            new_way = chosen_idx + [i]
            new_ways.append(new_way)
        return new_ways


s = Solution()
words = ["eebibfejchejb","jjeefifagb","hdgdhabhjeha","hajdbbheghe","bdbfhgebihffjec","fdcbaejhhibe","dabgifigigjjad","bejfhffjghhjfeh","gfbjebjjgfegeaf","fcijfdjjgd"]
letters = ["a","a","a","a","a","a","a","b","b","b","b","b","b","b","c","c","c","c","c","c","c","d","d","e","e","e","f","f","f","f","f","f","g","g","g","g","g","g","g","h","h","i","i","i","i","i","j","j"]
score = [4,8,3,1,3,5,3,4,7,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a = s.maxScoreWords(words, letters, score)
print(a)