class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.find_next_letter((i, j), 0, board, word, visited):
                    return True
        return False

    def find_next_letter(self, coordinate, curr_letter_index, board, word, visited):
        i = coordinate[0]
        j = coordinate[1]
        if visited[i][j]:
            return False
        if board[i][j] == word[curr_letter_index]:
            if curr_letter_index == len(word) - 1:
                return True
            # find next letter
            visited[i][j] = True
            up = self.find_next_letter((i - 1, j), curr_letter_index + 1, board, word, visited) if i > 0 else False
            left = self.find_next_letter((i, j - 1), curr_letter_index + 1, board, word, visited) if j > 0 else False
            right = self.find_next_letter((i, j + 1), curr_letter_index + 1, board, word, visited) if j < len(board[0]) - 1 else False
            down = self.find_next_letter((i + 1, j), curr_letter_index + 1, board, word, visited) if i < len(board) - 1 else False
            visited[i][j] = False
            return up or left or right or down
        else:
            return False

def test():
    s = Solution()
    r = s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
    q = s.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa")
    print(r, q)

test()