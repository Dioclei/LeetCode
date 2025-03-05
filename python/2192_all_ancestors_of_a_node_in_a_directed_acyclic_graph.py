from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # this algorithm doesn't work with cyclic graphs
        # use sets to prevent duplicates, and for easy sorting

        direct_parents = [set() for i in range(n)]
        answers = [set() for i in range(n)]
        done = [False for i in range(n)]

        # index all direct parents of each node
        for edge in edges:
            parent, child = edge[0], edge[1]
            direct_parents[child].add(parent)

        for i in range(n):
            self.add_ancestors(i, answers, direct_parents, done)

        # convert set to list
        answers = [sorted(s) for s in answers]
        return answers
    
    def add_ancestors(self, child, answers, direct_parents, done):
        for parent in direct_parents[child]:
            answers[child].add(parent)
            if done[parent]:
                for node in answers[parent]:
                    answers[child].add(node)
            else:
                # traverse parent
                for node in self.add_ancestors(parent, answers, direct_parents, done):
                    answers[child].add(node)
        done[child] = True
        return answers[child]


edges = [[4,0],[0,5],[3,0],[6,3],[4,5],[2,6],[6,5],[4,3],[2,0]]
n = 8
sol = Solution()
print(sol.getAncestors(n, edges))
