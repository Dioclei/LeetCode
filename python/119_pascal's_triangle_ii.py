# Problem: Given a row index, compute a row in Pascal's Triangle (0-indexed)
# Intuition:
# - Similar to 118, for any computation of a new row, we need the results of the previous row
# - This can be computed with a DP pattern of caching the previous results to compute the next result

# Comments:
# - this approach works, but uses more space than necessary
# - a more space-efficient method uses only 1 array. It is possible to modify the current row to output the new row.
# - for example, if the current row is [1, 3, 3, 1], the next row is [1, 4, 6, 4, 1].
# - we can compute this by appending a 1, then modify and overwrite the original row starting from the back, i.e. 1->4, 3->6, 3->4

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prevRow = self.getRow(rowIndex - 1)
            result = []
            result.append(1)
            for p in range(1, len(prevRow)):
                result.append(prevRow[p-1] + prevRow[p])
            result.append(1)
            return result

