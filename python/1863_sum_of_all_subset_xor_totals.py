from typing import List
from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # brute force
        # generate power set
        ps = []
        for i in range(len(nums) + 1):
            ps = ps + list(combinations(nums, i))

        xor_sum = 0
        for item in ps:
            if len(item) == 0:
                continue
            # calculate XOR total of item
            item_xor_total = item[0]
            for i in range(1, len(item)):
                item_xor_total = item_xor_total ^ item[i]
            xor_sum += item_xor_total
        
        return xor_sum

s = Solution()
p = s.subsetXORSum([1, 3])
print(p)