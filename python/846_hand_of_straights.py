from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        curr_val = None
        group_count = 0
        while len(hand) > 0:
            if curr_val is None:
                curr_val = hand.pop(0)
                group_count = group_count + 1
            else:
                curr_val = curr_val + 1
                if not self.find(hand, curr_val):
                    return False
                group_count = group_count + 1
            if group_count == groupSize:
                group_count = 0
                curr_val = None
        if group_count != 0:
            return False
        return True

    def find(self, hand, target):
        for idx, x in enumerate(hand):
            if x == target:
                hand.pop(idx)
                return True
            elif x > target:
                return False
        return False
            
sol = Solution()
result = sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)
print(result)