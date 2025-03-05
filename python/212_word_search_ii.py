# check if a list of words is present in a matrix
# for each word, do a simple dfs with their starting letter
# - if starting letter is not present then the word doesn't exist
# - keep track of visited positions to not revisit the same letter twice

# this solution is ok for brute force i think, but is not good enough for a leetcode hard
# can optimise by using a Trie to index all the words in the words list, this means you only need to check each prefix once
# so in the case of words like "abcdefg", "abcdefh", "abcdefi" the prefix "abcdef" only needs to be checked once

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        
        for word in words:
            first_letter = word[0]
            starting_positions = []      
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == first_letter:
                        starting_positions.append((i, j))
            word_found = False
            for pos in starting_positions:
                # conduct dfs with backtracking
                stack = [(pos, 0, set([pos]))] # stack contains: board position of new character, word idx of new character, visited positions
                if word_found: # if word was previously found, don't need to check more positions
                    break
                while len(stack) > 0:
                    board_pos, word_pos, visited = stack.pop()
                    # check if this is the end of the word
                    if word_pos == len(word) - 1:
                        word_found = True
                        result.append(word)
                        break
                    # check next positions
                    x, y = board_pos
                    # up
                    if y>0:
                        new_board_pos = (x, y-1)
                        if new_board_pos not in visited and board[new_board_pos[0]][new_board_pos[1]] == word[word_pos+1]:
                            v = visited.copy()
                            v.add(new_board_pos)
                            stack.append((new_board_pos, word_pos+1, v))
                    # down
                    if y<len(board[0])-1:
                        new_board_pos = (x, y+1)
                        if new_board_pos not in visited and board[new_board_pos[0]][new_board_pos[1]] == word[word_pos+1]:
                            v = visited.copy()
                            v.add(new_board_pos)
                            stack.append((new_board_pos, word_pos+1, v))
                    # left
                    if x>0:
                        new_board_pos = (x-1, y)
                        if new_board_pos not in visited and board[new_board_pos[0]][new_board_pos[1]] == word[word_pos+1]:
                            v = visited.copy()
                            v.add(new_board_pos)
                            stack.append((new_board_pos, word_pos+1, v))
                    # right
                    if x<len(board)-1:
                        new_board_pos = (x+1, y)
                        if new_board_pos not in visited and board[new_board_pos[0]][new_board_pos[1]] == word[word_pos+1]:
                            v = visited.copy()
                            v.add(new_board_pos)
                            stack.append((new_board_pos, word_pos+1, v))
            
        return result

            

s = Solution()
board = [["a","a"]]
words = ["aaa"]
print(s.findWords(board, words))
