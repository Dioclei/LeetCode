from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # implement union find
        rows = len(grid)
        cols = len(grid[0])
        parent = [[(r, c) for c in range(cols)] for r in range(rows)]

        # for each island, calculate their idx, union with left or top neighbours
        for r in range(rows):
            for c in range(cols):
                # check if water
                if grid[r][c] == '0':
                    # ignore
                    continue
                # if left side is land, union
                if r > 0 and grid[r-1][c] == '1':
                    self.union((r, c), (r-1, c), parent)
                # if top side is land, union
                if c > 0 and grid[r][c-1] == '1':
                    self.union((r, c), (r, c-1), parent)

        print(parent)
        # count the number of groups
        groups = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                else:
                    group = self.find((r, c), parent)
                    groups.add(group)
        return len(groups)

    def find(self, idx, parent):
        r = idx[0]
        c = idx[1]
        if parent[r][c] != idx:
            return self.find(parent[r][c], parent)
        else:
            return (r, c)
        
    def union(self, idx1, idx2, parent):
        # connects the root of idx1 to the root of idx2
        r1, c1 = self.find(idx1, parent)
        r2, c2 = self.find(idx2, parent)
        parent[r1][c1] = parent[r2][c2]

    # EDITORIAL:
    # can use bfs or dfs, it is the same time complexity.

sol = Solution()
map = [["1","1","0","0","0"],
       ["1","1","0","0","0"],
       ["0","0","1","0","0"],
       ["0","0","0","1","1"]]
print(sol.numIslands(map))

        

