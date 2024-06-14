from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        contains = set()
        # check every row
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in contains:
                    print('row wrong')
                    return False
                else:
                    contains.add(val)
            contains.clear()

        # check every column
        for col in range(9):
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in contains:
                    print('col wrong')
                    return False
                else:
                    contains.add(val)
            contains.clear()
        
        # check every grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        row = i + k
                        col = j + l
                        val = board[row][col]
                        if val == ".":
                            continue
                        if val in contains:
                            return False
                        else:
                            contains.add(val)
                contains.clear()
        
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudoku(board))