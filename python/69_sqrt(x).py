# Search problem: Find the square root of some integer, rounded down to the nearest integer
# Intuition
# - search for an integer
# - we can check if an integer is a square root by squaring it
# - use binary search to find the best candidate integer

class Solution:
    def mySqrt(self, x: int) -> int:
        # look for a square root in the range 0 - x
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            if square > x:
                high = mid - 1
            else:
                low = mid + 1
        # we want the square root rounded down
        # return high because when the while loop ends, high^2 will always be < x
        return high