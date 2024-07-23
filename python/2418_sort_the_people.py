from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = list(zip(heights, names))
        combined.sort(reverse=True)
        result = []
        for item in combined:
            result.append(item[1])
        return result


