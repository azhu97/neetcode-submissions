class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
            res += 1
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if dp[i][j] or i > j:
                    continue
                if s[i] == s[j] and ((dp[i + 1][j - 1]) or j - i == 1):
                    dp[i][j] = True
                    res += 1
        
        return res
            