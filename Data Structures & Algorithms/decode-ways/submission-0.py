class Solution:
    def numDecodings(self, s: str) -> int:
        # a string of upper 
        # A -> 1, B -> 2, ..., Z -> 26
        # there are mulitple ways to decode a message
        # 1012 -> 10 1 2 | 10 12
        # dp[i] tells us how many ways we can decode s[::i], including i
        # dp[i] = dp[i-1] + + 1 + (1 if s[i - 1] <= 2 else 0)
        dp = [0 for i in range(len(s))]
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            dp[i] = dp[i - 1] + (1 if (ord(s[i]) - ord('0') <= 6 and 0 < ord(s[i-1]) - ord('0') <= 2) else 0)
        
        print(dp)
        return dp[-1]