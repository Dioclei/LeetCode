from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # need to find no. of days
        # max days = max(bloomDay)
        # min days = min(bloomDay)
        # use binary search to find the minimum number of days
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = low + (high - low) // 2
            if self.is_possible_to_make_bouquets(bloomDay, m, k, mid):
                high = mid - 1
            else:
                low = mid + 1
        if self.is_possible_to_make_bouquets(bloomDay, m, k, low):
            return low
        else:
            return -1

    def is_possible_to_make_bouquets(self, bloomDay, m, k, days):
        bouquets = 0
        flowers = 0
        for flower in bloomDay:
            if flower <= days:
                # pick a flower
                flowers += 1
            else:
                flowers = 0
            if flowers == k:
                # create a bouquet
                bouquets += 1
                flowers = 0
        if bouquets >= m:
            return True
        else:
            return False
        
    # to understand binary search:
    # 1. understand intervals       (starting values for low and high, and whether to use <=)
    # 2. understand partition       (to partition properly, there should be 3 non-overlapping partitions)
    # 3. understand exit condition  (how to get what you want out of the search)
        
sol = Solution()
bloomDay = [1,10,3,10,2]
m = 3
k = 2
print(sol.minDays(bloomDay, m, k))