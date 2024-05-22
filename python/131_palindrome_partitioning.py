from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # start from empty list, at every step, either
        # 1. add new element as a partition
        # 2. add new element to the last element

        palindromes = set()
        partitions = []
        def helper(p, i):
            if i == len(s) - 1:
                # make sure that all p in partition are palindromes
                for pa in p:
                    if pa in palindromes:
                        continue
                    if self.palindrome_check(pa):
                        palindromes.add(pa)
                    else:
                        return False
                # add the new partition to the partition list
                partitions.append(p)
                return
            next_i = i + 1
            # 1. add new element as a partition
            new_p = p + [s[next_i]]
            helper(new_p, next_i)
            # 2. add new element to the last element
            if len(p) == 0:
                return
            new_p = p.copy()
            new_p[-1] = new_p[-1] + s[next_i]
            helper(new_p, next_i)

        helper([], -1)
        return partitions

    
    def palindrome_check(self, p: str) -> bool:
        p1 = 0
        p2 = len(p) - 1
        while p1 <= p2:
            if p[p1] != p[p2]:
                return False
            p1 = p1 + 1
            p2 = p2 - 1
        return True
    

solution = Solution()
print(solution.palindrome_check("a"))
print(solution.partition("aab"))