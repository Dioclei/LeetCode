# medium

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        a = b = float('inf')
        for x in nums:
            if x < b and x < a:
                a = x
            if x < b and x > a:
                b = x
            if x > b:
                return True
        return False
            