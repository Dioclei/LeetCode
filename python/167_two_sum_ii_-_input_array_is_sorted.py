from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # need to find the exact sum, cannot reuse numbers
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            sum = numbers[p1] + numbers[p2]
            if sum < target:
                p1 += 1
            elif sum > target:
                p2 -= 1
            else:
                return [p1 + 1, p2 + 1]
        return False # provided test cases shouldn't be invalid so the code should not reach here