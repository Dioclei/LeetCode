class Solution:
    def checkRecord(self, n: int) -> int:
        # 2 criteria for the sequence to be valid: 
        # sequence contains < 2 'A'
        # sequence contains 'L' chains of at most < 3 length

        # create 2d DP array containing: 
        # number of sequences at any one day m <= n,
        # which pertain to having 0/1 'A's, and the last values being 0/1/2 consequtive 'L's
        # this array will be modified in-place
        # L \ A 0 1
        # 0     
        # 1
        # 2

        dp = [[0 for i in range(2)] for j in range(3)]
        new_dp = [[0 for i in range(2)] for j in range(3)]

        if n == 0:
            return 0
        # key in first day values
        dp[0][0] = 1
        dp[0][1] = 1
        dp[1][0] = 1

        m = 1
        while m < n:
            # writing code based on result:
            new_dp[0][0] = sum(dp[i][0] for i in range(3)) # + P
            new_dp[0][1] = sum(dp[i][j] for i in range(3) for j in range(2)) # + A or + P
            # + L
            for i in range(1, 3):
                for j in range(2):
                    new_dp[i][j] = dp[i - 1][j]
            # copy dp array
            for i in range(3):
                for j in range(2):
                    dp[i][j] = new_dp[i][j] % (10**9 + 7)
            m += 1
        
        # sum everything
        s = sum([sum(arr) for arr in dp])
        return s % (10**9 + 7)
        
    
sol = Solution()
p = sol.checkRecord(2)
print(p)
            
        
        
