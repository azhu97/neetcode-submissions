class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] represents if i -> j is 
        # base case: dp[i][0] = True
        # actually the base case is not true, dp[i][j] = True if i == j
        # we iterate left to right, bottom to top 
        # checking, does s[i:j+1] form a palindrome? 
        # this is only True if s[i] == s[j] and dp[i + 1][j - 1] is true
        res_i, res_j = 0, 0
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if dp[i][j] or i > j:
                    continue
                if s[i] == s[j] and ((dp[i + 1][j - 1]) or j - i == 1):
                    dp[i][j] = True
                    if (j - i) > (res_j - res_i):
                        res_i, res_j = i, j
        # for arr in dp:
            # print(arr)
        return s[res_i:res_j+1]


        # are there odd vs even cases