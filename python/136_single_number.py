# Problem: Given a non-empty array containing integers that only appear twice except for one, find the integer that appears once
# Constraint: Solve in linear time and constant space complexity (i.e. no nested looping, no hashmap)
# Intuition:
# - Since there is a need to solve it in linear time and constant space complexity, we need to somehow manipulate the numbers with an intermediate result
# - XOR is suitable in this case because:
#   - the XOR of 2 of the same number is 0
#   - the XOR of 0 and some number x is x.
#   - the XOR of 0 and 0 is 0
#   - XOR is commutative, so the order of XORs applied doesn't matter.
# - Hence, if XOR is applied to the whole array, we will obtain the number that doesn't have a duplicate.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result