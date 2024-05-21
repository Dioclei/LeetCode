from typing import List
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # combinations solution
        # result = []
        # for i in range(len(nums) + 1):
        #     result = result + list(combinations(nums, i))
        # return result
        
        # recursive solution, O(2^N)
        visited = set()
        def helper(nums, visited):
            s = [nums] # include complete subset
            for i in range(len(nums)):
                # pop an element, check whether it is visited
                new_nums = nums.copy()
                new_nums.pop(i)
                if tuple(new_nums) not in visited:
                    visited.add(tuple(new_nums))
                    s = s + helper(new_nums, visited) # add subsets where a value is popped
            return s
        return helper(nums, visited)

p = Solution()
print(p.subsets([0]))