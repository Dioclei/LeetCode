from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # calculate all subarray sums
        m = 10**9 + 7
        subarray_sums = []
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum = (sum + nums[j])
                subarray_sums.append(sum)
        subarray_sums.sort()
        result = 0
        for k in range(left - 1, right):
            result += subarray_sums[k]
            result = result % m
        return result


