from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # let's have a slow runner and a fast runner. 
        # fast runner will find all the dupes. 
        # slow runner will keep track of the last unique element
        p1 = 0 # slow runner
        p2 = 0 # fast runner
        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                nums[p1 + 1] = nums[p2]
                p1 = p1 + 1
            else:
                p2 = p2 + 1
        return p1 + 1
    
sol = Solution()
l = [1, 2, 2, 2, 2, 3, 3]
print(sol.removeDuplicates(l))
print(l)

