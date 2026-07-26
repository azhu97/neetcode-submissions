class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp of length i and j, where dp[i][j] = longest subsequence up to i and j
        # there are a few decisions to make
        # if t1[i] == t2[j], dp[i][j] = dp[i-1][j-1] + 1
        # if they do not match, we can just take from the largest adjacent dp
        # because theres no harm in taking the largest
        dp = [[0 for j in range(len(text1) + 1)] for i in range(len(text2) + 1)]
        for j in range(1, len(dp[0])):
            for i in range(1, len(dp)):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
        