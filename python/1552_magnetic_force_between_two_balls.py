from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        total_dist = position[-1] - position[0]
        hi = total_dist // (m-1)
        lo = 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.is_possible(position, m, mid):
                # it is possible to put balls mid distance apart, attempt to increase distance
                lo = mid + 1
            else:
                # not possible, decrease distance
                hi = mid - 1
        return hi

    def is_possible(self, position, m, dist):
        # attempt to put m balls into position, dist distance apart
        # put a ball at first position
        m -= 1
        p = 1
        curr_dist = 0
        while p < len(position):
            curr_dist += position[p] - position[p-1]
            if curr_dist >= dist:
                # put a ball
                curr_dist = 0
                m -= 1
            p += 1
        if m <= 0:
            return True
        else:
            return False
        
sol = Solution()
position = [1,2,3,4,7]
m = 2
print(sol.maxDistance(position, m))
print(sol.is_possible(position, m, 6))
        