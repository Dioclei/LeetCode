import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.floor(math.sqrt(c)))
        while a <= b:
            # check if a^2 + b^2 = c
            sum = a * a + b * b
            if sum == c:
                return True
            
            # 2 pointer solution
            # O(sqrt(c))
            if sum > c:
                b -= 1
            else:
                a += 1
            
        return False

sol = Solution()
print(sol.judgeSquareSum(2))
