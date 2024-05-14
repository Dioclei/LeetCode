# easy

# find last zero and last number before a zero
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # start from the back to find last zero, and subsequently last non-zero
        zero_found = False
        p1 = None
        p2 = None
        for i in range(len(nums) - 1, -1, -1):
            if not zero_found and nums[i] == 0:
                p1 = i
                zero_found = True
            elif zero_found and nums[i] != 0:
                p2 = i
                break
        # swap every last non-zero with the last zero
        while p1 > -1:
            if nums[p1] == 0:
                while nums[p2] == 0:
                    p2 -= 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 -= 1
        
