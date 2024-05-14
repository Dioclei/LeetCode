# medium

class Solution(object):

    def __init__(self) -> None:
        self.m = 1000000007
        self.number_of_tilings = {}

    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_row = []
        second_row = []
        self.dp(first_row, second_row, 1, n)
        count = 0
        for i in range(1, n + 1):
            count += self.number_of_tilings[i]
        count = count % self.m
        return count
        
    def dp(self, f, s, n, max_n):
        if n > max_n:
            return
        spaces_first_row = n - len(f)
        spaces_second_row = n - len(s)
        if spaces_first_row == 2 and spaces_second_row == 2:
            # fit a tromino two ways
            # 1
            self.dp(f + [1, 1], s + [1], n + 1, max_n)
            # 2
            self.dp(f + [1], s + [1, 1], n + 1, max_n)
            # fit two dominoes
            self.dp(f + [1, 1], s + [1, 1], n + 1, max_n)
            self.add_one(n)
        elif spaces_first_row == 2 and spaces_second_row == 1:
            # fit a tromino
            self.dp(f + [1, 1], s + [1], n + 1, max_n)
            self.add_one(n)
            # fit a domino
            self.dp(f + [1, 1], s, n + 1, max_n)
        elif spaces_first_row == 1 and spaces_second_row == 2:
            # fit a tromino
            self.dp(f + [1], s + [1, 1], n + 1, max_n)
            self.add_one(n)
            # fit a domino
            self.dp(f, s + [1, 1], n + 1, max_n)
        elif spaces_first_row == 1 and spaces_second_row == 1:
            # fit a domino
            self.dp(f + [1], s + [1], n + 1, max_n)
            self.add_one(n)
            # dont fit anything, add one more to space
            self.dp(f, s, n + 1, max_n)
        else:
            print("error")
    
    def add_one(self, n):
        if n not in self.number_of_tilings:
            self.number_of_tilings[n] = 1
        else:
            self.number_of_tilings[n] = self.number_of_tilings[n] + 1
        self.number_of_tilings[n] = self.number_of_tilings[n] % self.m

s = Solution()
print(s.numTilings(3))
