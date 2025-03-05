from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for senior_detail in details:
            age = senior_detail[11:13]
            if int(age) > 60:
                count += 1
        return count