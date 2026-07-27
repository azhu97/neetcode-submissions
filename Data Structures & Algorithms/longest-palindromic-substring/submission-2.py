class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i] = longest palindromic substring including s[i]
        # at dp[i], we want to look for the largest number
        # we can iterate from 0 to i - 1, call j, and see which dp[j] is the largest
        # with the condition
        # if dp[i] = dp[i - 1] + 1 if s[i] = s[i - dp[i - 1]] else 1
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        highest = 1
        index = 0
        for i in range(1, len(s)):
            dp[i] = 1
            for j in range(i):
                # print(i, j)
                # print(s[i] == s[j], (i - j - 1) <= dp[i - 1], dp[i - 1])
                if (s[i] == s[j] and (i - j - 1) <= dp[i - 1] and i - dp[i - 1] != j) or s[i] == s[j] and i - j == 1:
                    dp[i] = max(dp[i], i - j + 1)
                    if dp[i] > highest:
                        highest, index = dp[i], i
        
        print(dp)
        return s[index - highest + 1 : index + 1]