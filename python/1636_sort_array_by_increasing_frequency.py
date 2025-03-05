from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # initialise a frequency map
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # custom comparator, 1. freq[num] (ascending), 2. num (descending with negative sign)
        nums.sort(key=lambda num: (freq[num], -num)) 
        return nums