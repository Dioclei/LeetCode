from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # i can remove the last term by xor-ing the last term again
        i = 0
        j = len(arr) - 1
        k = j
        for m in range(i, j):
            