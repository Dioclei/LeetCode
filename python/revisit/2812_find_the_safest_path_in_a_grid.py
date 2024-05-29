from typing import List
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # 1. find for each cell, the minimum distance to any thief using BFS with PQ
        # should be O(n * nlogn)

        n = len(grid)
        dist_from_nearest_thief = [[99999999 for i in range(n)] for i in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                q.clear()
                q.append((0, i, j))
                while len(q) > 0:
                    dist, trav_i, trav_j = q.pop(0)
                    # check if this is a thief, then update the safeness of original square
                    if grid[trav_i][trav_j] == 1:
                        dist_from_nearest_thief[i][j] = dist
                    # find neighbours
                    neighbours = []
                    if trav_i > 0:
                        neighbours.append((dist + 1, trav_i - 1, trav_j))
                    if trav_j > 0:
                        neighbours.append((dist + 1, trav_i, trav_j - 1))
                    if trav_i < n - 1:
                        neighbours.append((dist + 1, trav_i + 1, trav_j))
                    if trav_j < n - 1:
                        neighbours.append((dist + 1, trav_i, trav_j + 1))
                    for neighbour in neighbours:
                        heapq.heappush(q, neighbour)

        print(dist_from_nearest_thief)

        # 2. find maximum total safeness from (0, 0) to (1, 1)
        # safeness = min of dist from thief from all cells
        # index each node with the min of all distances in that path
        # we want to maximise this distance, so we use a maxheap, i.e. negative the value
        q.clear()
        heapq.heappush(q, (-dist_from_nearest_thief[0][0], 0, 0))
        visited = set()
        while len(q) > 0:
            dist, trav_i, trav_j = heapq.heappop(q)
            visited.add((trav_i, trav_j))
            dist = -dist
            if trav_i == n - 1 and trav_j == n - 1:
                return dist
            neighbours = []
            if trav_i > 0 and (trav_i - 1, trav_j) not in visited:
                neighbours.append((-min(dist, dist_from_nearest_thief[trav_i - 1][trav_j]), trav_i - 1, trav_j))
            if trav_j > 0 and (trav_i, trav_j - 1) not in visited:
                neighbours.append((-min(dist, dist_from_nearest_thief[trav_i][trav_j - 1]), trav_i, trav_j - 1))
            if trav_i < n - 1 and (trav_i + 1, trav_j) not in visited:
                neighbours.append((-min(dist, dist_from_nearest_thief[trav_i + 1][trav_j]), trav_i + 1, trav_j))
            if trav_j < n - 1 and (trav_i, trav_j + 1) not in visited:
                neighbours.append((-min(dist, dist_from_nearest_thief[trav_i][trav_j + 1]), trav_i, trav_j + 1))
            for neighbour in neighbours:
                heapq.heappush(q, neighbour)
                

s = Solution()
d = s.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
print(d)