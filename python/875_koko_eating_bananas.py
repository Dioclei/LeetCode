# use binary search to search for the smallest k (eating speed) to finish eating all the bananas
# lower bound of k is the minimum speed to eat all bananas. 
# - this is easily computed by dividing total bananas by hours
# upper bound of k is the maximum speed to eat all bananas. 
# - a sensible number is the maximum of all piles, meaning she finishes that pile in 1 hour.
# - having a higher speed wouldn't make sense because it will not make her faster because she can already eat the largest pile in 1 hour

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_banana = 0
        for banana_count in piles:
            max_banana = max(max_banana, banana_count)
        lower = (max_banana-1) // h + 1 # or use math.ceil()
        upper = max_banana
        while lower < upper:
            print("lower: ", lower, "upper: ", upper)
            mid = lower + (upper - lower) // 2
            eating_time_needed = self.eating_time_needed(piles, mid)
            print("eating time: ", eating_time_needed)
            # even if she can eat all bananas at this speed within the time limit, we want to lower the speed
            # so as long as eating time needed <= h, we need to try to reduce the number by reducing the upper bound
            if eating_time_needed <= h:
                upper = mid
            else:
                lower = mid+1
        # lower == upper now, so return
        return lower

    def eating_time_needed(self, piles, speed):
        total_time_needed = 0
        for banana_count in piles:
            time_needed = (banana_count-1) // speed + 1
            total_time_needed += time_needed
        return total_time_needed
    
s = Solution()
r = s.minEatingSpeed([1, 3, 5], 5)
print(r)