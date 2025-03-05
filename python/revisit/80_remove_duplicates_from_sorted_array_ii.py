from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # have a slow runner and fast runner
        p_slow = 0 # current slow runner idx
        p_fast = 1 # current fast runner idx
        p_slow_count = 0 # number of characters counted by slow runner, at the current slow runner idx

        while p_fast < len(nums):
            # check fast runner value
            if nums[p_fast] != nums[p_slow]:
                nums[p_slow], nums[p_fast] = nums[p_fast], nums[p_slow]
                p_slow_count = 1
                p_slow += 1
                p_fast += 1
            else:
                if p_slow_count < 2:
                    nums[p_slow] = nums[p_fast]
                    p_slow_count += 1
                    p_slow += 1
                    p_fast += 1
                else:
                    p_fast += 1

sol = Solution()
nums = [1, 1, 1, 1, 2, 2, 2, 3, 4]
sol.removeDuplicates(nums)
print(nums)