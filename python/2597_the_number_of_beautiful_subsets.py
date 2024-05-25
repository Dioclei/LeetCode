from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # sort the list for easier validation for dp later
        nums.sort()
        
        subsets = [[]]
        for index, val in enumerate(nums):
            for subset in subsets.copy():
                # attempt to create new subset
                if len(subset) > 0 and not self.validateSubset(subset, val, k):
                    # if the new subset is an invalid subset, adding more elements will not make it valid.
                    continue
                # add in new element to make a new subset
                new_subset = subset + [val]
                subsets.append(new_subset)
        return len(subsets) - 1 # -1 for empty subset

    def validateSubset(self, old_subset, new_val, k):
        # check old subset for new_val - k:
        target = new_val - k
        # if old_subset contains target, then it is not valid.
        # quick O(1) check subset range
        if old_subset[0] > target or old_subset[-1] < target:
            return True
        else:
            # binary search for target
            p1 = 0
            p2 = len(old_subset) - 1
            while p1 <= p2:
                mid = (p1 + p2) // 2
                val = old_subset[mid]
                if p1 == p2 and val != target:
                    return True
                if target < val:
                    p2 = mid
                elif target > val:
                    p1 = mid + 1
                else:
                    # target found
                    return False
            return True

