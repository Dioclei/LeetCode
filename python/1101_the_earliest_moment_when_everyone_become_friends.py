from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort the logs by timestamp
        logs.sort()
        parent = [i for i in range(n)]
        group_count = n
        for log in logs:
            timestamp, p1, p2 = log[0], log[1], log[2]
            group_count = self.union(p1, p2, parent, group_count)
            if group_count == 1:
                return timestamp
        return -1

    def union(self, x, y, parent, group_count):
        group1 = self.find(x, parent)
        group2 = self.find(y, parent)
        if group1 != group2:
            parent[group2] = group1
            return group_count - 1
        return group_count
    
    def find(self, x, parent):
        if parent[x] == x:
            return x
        else:
            return self.find(parent[x], parent)