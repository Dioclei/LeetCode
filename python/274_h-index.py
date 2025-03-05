from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # find the maximum h such that
        # there are at least h papers 
        # that have been cited at least h times

        # sort citations
        citations.sort()
        # go along the citations, at any index i: 
        # there are at least len(citations) - (i) papers with at least citations[i] citations
        for i in range(len(citations)):
            papers = len(citations) - i
            num = citations[i]
            if num >= papers:
                return papers
        return 0