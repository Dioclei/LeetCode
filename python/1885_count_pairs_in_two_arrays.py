from math import comb

class Solution:
    def countPairs(self, nums1: list[int], nums2: list[int]) -> int:

        if len(nums1) <= 1:
            return 0

        diff = []
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            diff.append(d)
        diff.sort()
        # diff will have positive values and negative values.
        # the goal is to pair the negative values with as many positive values as possible
        # such that the positive values balance out the negative values

        count = 0
        p1 = 0
        p2 = len(diff) - 1

        # find pairs for the non-positive values first
        while diff[p1] <= 0:
            # deduct from p2 until diff[p2] cannot balance out diff[p1]
            while diff[p2] + diff[p1] > 0:
                p2 -= 1
            # count from the back to know how many positive pairs can balance out the current negative pair
            count = count + (len(diff) - 1 - p2)
            p1 += 1
        # now p1 is at the first positive value
        # all positive differences make good pairs together, hence we can simply use a formula
        count = count + comb(len(diff) - p1, 2)
        return count

s = Solution()
print(s.countPairs([2,1,2,1], [1,2,1,2]))
        


