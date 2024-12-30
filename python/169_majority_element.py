# Problem: find the majority element that appears > n/2 times in a list. It is guaranteed to appear.
# Intuition:
# - Count the number of times each element appears and take the value that appears > n/2 times

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_val = len(nums) // 2
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            if count[n] > majority_val:
                return n
        raise Error("should not reach here")