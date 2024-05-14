# easy

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score_sorted = score.copy()
        score_sorted.sort(reverse=True)
        def getRank(i):
            if i == 0:
                return "Gold Medal"
            if i == 1:
                return "Silver Medal"
            if i == 2:
                return "Bronze Medal"
            return str(i + 1)
        rank = {x: getRank(i) for i, x in enumerate(score_sorted)}
        score = [rank[x] for x in score]
        return score
    
