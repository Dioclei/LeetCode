# n^2 connected graph solution. reacheds TLE on leetcode. pls use the other sorting solution.

from typing import List
from collections import defaultdict

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # create a graph containing visited intervals. overlapping intervals are connected
        graph = defaultdict(list)
        for i in range(len(intervals)):
            interval1 = tuple(intervals[i])
            graph[interval1].append(interval1)
            for j in range(i+1, len(intervals)):
                interval2 = tuple(intervals[j])
                if self.has_overlap(interval1, interval2):
                    graph[interval1].append(interval2)
                    graph[interval2].append(interval1)
        new_intervals = set()
        for key in graph:
            # compute the connected graph
            connecteds = self.compute_connected_graph(graph, key)
            new_int = self.compute_new_interval(connecteds)
            new_intervals.add(new_int)

        result = list(new_intervals)
        result.sort(key=lambda a: a[0])
        return result

    def has_overlap(self, interval1, interval2):
        x1, y1 = interval1
        x2, y2 = interval2
        cond1 = (x1 <= y2) and (y1 >= x2)
        cond2 = (x2 <= y1) and (y2 >= x1)
        return cond1 or cond2
    
    def compute_new_interval(self, intervals):
        min_x, max_y = intervals[0]
        for item in intervals:
            x, y = item
            min_x = min(min_x, x)
            max_y = max(max_y, y)
        return (min_x, max_y)
    
    def compute_connected_graph(self, graph, key):
        # traverse each connected component with dfs
        stack = list(graph[key])
        visited = set()
        while (len(stack) > 0):
            item = stack.pop()
            if item in visited:
                continue
            # visit item
            visited.add(item)
            # add item's neighbours to stack
            for other in graph[item]:
                stack.append(other)
        return list(visited)

s = Solution()
input = [[1,4],[0,2],[3,5]]
print(s.merge(input))