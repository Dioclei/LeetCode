from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # important points in the array:
        # 0 - where 0 starts
        # p1 - where 1 starts
        # p2 - where 2 starts
        p1 = p2 = p3 = 0
        while p3 < len(nums):
            # check value at p3
            if nums[p3] == 0:
                # put at end of 0 part, swap values along
                # cannot do pythonic swap because it will overwrite some values, need to do step by step
                temp = nums[p3]
                nums[p3] = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = temp
                p1, p2, p3 = p1 + 1, p2 + 1, p3 + 1
            elif nums[p3] == 1:
                # put at end of 1 part, swap values along
                nums[p2], nums[p3] = nums[p3], nums[p2]
                p2, p3 = p2 + 1, p3 + 1
            else:
                # is already at end of 2 part, just update pointer
                p3 = p3 + 1

    
    # EDITORIAL SOLUTION:

    # my solution involves swapping the colors brute force
    # but this editorial solution is much better, partitioning the array into 3 parts using 2 pointers
    # maintain the invariant that the left side of p0 and right side of p2 are sorted. (i.e. left of p0 = 0, right of p2 = 2)
    # then make swaps accordingly in the middle partition
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # For all idx < p0 : nums[idx < p0] = 0
        # curr is an index of elements under consideration
        p0 = curr = 0

        # For all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

sol = Solution()
nums = [2, 1, 0, 0, 2, 1]
sol.sortColors(nums)
print(nums)

            
