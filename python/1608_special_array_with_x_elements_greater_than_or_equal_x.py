from typing import List
import heapq

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # O(nlogn) solution
        target_x = len(nums)
        heapq.heapify(nums)
        prev = -1
        while len(nums) > 0:
            x = heapq.heappop(nums)
            if x >= target_x and not prev >= target_x:
                return target_x
            target_x -= 1
            prev = x
        return -1