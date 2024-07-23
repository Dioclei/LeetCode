from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # change the list such that after removing 3 of the smallest or largest values, the difference is at a minimum.
        nums.sort()
        