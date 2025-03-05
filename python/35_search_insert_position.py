# Search problem
# - find the insertion index of a target in a sorted list
# Intuition
# - list is sorted, we are looking for something in a sorted list
# - use binary search to reduce search area

# Comments
# - as correctly done, we use binary search in this problem.
# - we always use binary search for searching for a singular target in a sorted list.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while low <= high: # define search space
            mid = (low + high) // 2
            # check if we found the target
            if target == nums[mid]:
                return mid
            # if we haven't found the target, partition the list accordingly
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        # low denotes the idx that the target should be at.
        # this is because we move low up when the target is higher than mid, 
        # and keep low the same when the target is smaller.
        # note that we don't always return low but in this case it works for the insertion index.
        return low
        
