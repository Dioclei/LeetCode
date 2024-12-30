# Problem: given a lower bound and an upper bound, and a sorted list of numbers, find the (most efficient) ranges of values that are not in the list
# Intuition:
# - we can think of the number list as slicing up the bound into ranges
# - keep a lower and upper pointer for the current range, and process the number list to see how the range changes
# - invariant: any range that is before the current number cannot be changed, so we can append it to the result
# - e.g. if the lower bound is 0 and the first number is 2, then we know [0, 1] is definitely in the result

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # set values for the current range
        pLower = lower
        pUpper = upper
        result = []
        # process number list
        for n in nums:
            if n == pLower:
                # move pLower up
                pLower += 1
            elif n > pLower:
                # make a cut to n-1, and move pLower up
                new_range = [pLower, n-1]
                result.append(new_range)
                pLower = n+1
            else:
                # not possible
                raise Error("not possible")
        if pLower <= pUpper:
            result.append([pLower, pUpper])
        return result