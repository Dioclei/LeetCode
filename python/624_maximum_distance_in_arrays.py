from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # find the smallest number from the left side
        # find the largest number from the right side
        s = arrays[0][0]
        l = arrays[0][-1]
        for array in arrays:
            if array[0] < s:
                s = array[0]
            if array[-1] > l:
                l = array[-1]
        return abs(l - s)
