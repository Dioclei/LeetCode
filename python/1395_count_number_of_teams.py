from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # the idea is to count, for each middle number, the number of valid values to its left and right
        # then multiply this two counts to get the number of sequences.
        # do this twice, once for ascending sequences and one for descending sequences

        total_sequence_count = 0
        for i in range(1, len(rating) - 1):
            left_less_than = 0
            left_more_than = 0
            right_less_than = 0
            right_more_than = 0
            for j in range(len(rating)):
                if j == i:
                    continue
                if j < i:
                    if rating[j] < rating[i]:
                        left_less_than += 1
                    else:
                        # all values are unique, they will not be equal
                        assert rating[j] != rating[i]
                        left_more_than += 1
                else:
                    if rating[j] < rating[i]:
                        right_less_than += 1
                    else:
                        assert rating[j] != rating[i]
                        right_more_than += 1
            total_sequence_count += (left_less_than * right_more_than + left_more_than * right_less_than)
            # reset values
            left_less_than, left_more_than, right_less_than, right_more_than = 0, 0, 0, 0
        return total_sequence_count

s = Solution()
print(s.numTeams([1, 2, 3, 4]))


                