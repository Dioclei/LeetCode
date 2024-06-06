from typing import List

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        intersection = arrays[0]
        for array in arrays[1:]:
            intersection = self.intersection_helper(intersection, array)
        return intersection
    
    def intersection_helper(self, array1, array2):
        # array1 and array2 are sorted
        p1 = 0
        p2 = 0
        intersection = []
        while p1 < len(array1) and p2 < len(array2):
            if array1[p1] == array2[p2]:
                intersection.append(array1[p1])
                p1 += 1
                p2 += 1
            elif array1[p1] < array2[p2]:
                p1 += 1
            else:
                p2 += 1
        return intersection