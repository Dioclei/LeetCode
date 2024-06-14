from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summary_ranges = []
        if len(nums) == 0:
            return summary_ranges
        start = nums[0]
        for i in range(1, len(nums)):
            # check if it is continuous
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                r = self.create_range(start, nums[i-1])
                summary_ranges.append(r)
                start = nums[i]
        # create the last range
        r = self.create_range(start, nums[-1])
        summary_ranges.append(r)
        return summary_ranges
    

    def create_range(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)

nums = [1, 2, 3, 4]
sol = Solution()
print(sol.summaryRanges(nums))
            