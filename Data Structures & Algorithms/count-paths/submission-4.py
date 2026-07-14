class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0] = [1] * n
        for i in range(1, m):
            dp[i][0] = 1
        print(dp)
        for i, arr in enumerate(dp):
            for j, value in enumerate(arr):
                if value == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m - 1][n - 1]
                