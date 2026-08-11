class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j], does s[::i] match p[::j]:
        # all starts false, except for 0, 0
        # so when is dp[i][j] True? 
        # we have to first look at s[i - 1], p[j - 1]
        # 1. s and p match, dp[i][j] = dp[i - 1][j - 1]
        # don't match 
        # p not * or . -> do[i][j] = False, simply not possible
        # p == ., dp[i][j] = dp[i - 1][i - j]
        # p == *, dp[i][j] -> we have to check the previous 0 to i [j]
        # find the nearest
        # we don't want to greedily fill out p, take it slow 
        # top to bottom, left to right
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        p_set = set() # keep track of previous
        for j in range(1, len(dp[0])):
            for i in range(1, len(dp)):
                print(i, j)
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # they don't match straight up
                    if p[j - 1] == '.':
                        dp[i][j] == dp[i - 1][j - 1]
                    elif p[j - 1] == '*':
                        if (dp[i][j-1] or dp[i - 1][j]) and s[i - 1] in p_set or '.' in p_set:
                            dp[i][j] = True
                        else:
                            dp[i][j] = False
            p_set.add(p[j - 1])

        return dp[-1][-1]