class Solution:
    # most brute force solution
    # def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
    #     n = len(grid)
    #     new_dim = n - 2
    #     result = [[0 for i in range(new_dim)] for j in range(new_dim)]
    #     for i in range(new_dim):
    #         for j in range(new_dim):
    #             start = (i, j)
    #             end = (i+2, j+2)
    #             local_max = 0
    #             for p in range(start[0], end[0] + 1):
    #                 for q in range(start[1], end[1] + 1):
    #                     local_max = max(local_max, grid[p][q])
    #             result[i][j] = local_max
    #     return result

    # still O(n^2) but should have slightly better time complexity
    # uses no extra memory, i.e. O(1) memory
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        for i in range(0, n - 2):
            for j in range(0, n - 2):
                grid[i][j] = max(grid[i][j], grid[i + 1][j], grid[i + 2][j])
        
        for i in range(0, n-2):
            for j in range(0, n-2):
                grid[i][j] = max(grid[i][j], grid[i][j + 1], grid[i][j + 2])

        return [grid[i][0:n-2]for i in range(0, n-2)]
    
s = Solution()
r = s.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
print(r)