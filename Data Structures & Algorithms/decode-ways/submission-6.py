class Solution:
    def numDecodings(self, s: str) -> int:
        # a string of upper 
        # A -> 1, B -> 2, ..., Z -> 26
        # there are mulitple ways to decode a message
        # 1012 -> 10 1 2 | 10 12
        # dp[i] tells us how many ways we can decode s[::i], including i
        # dp[i] = dp[i-1] + + 1 + (1 if s[i - 1] <= 2 else 0)
        first_set = set(['1', '2'])
        second_set = set(['7', '8', '9'])
        dp = [0 for i in range(len(s))]
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if s[i] == '0':
                dp[i] = dp[i - 1] if s[i - 1] != '0' else 0
            else:
                # s[i] != '0'
                # coupel scenarios
                # if s[i - 1] is 1 or 2, dp[i] = dp[i - 1] + 1
                # else if s[i - 1] is literally anything else, dp[i] = dp[i - 1]
                dp[i] = dp[i - 1]
                if s[i - 1] in first_set and s[i] not in second_set:
                    dp[i] += 1
        
        print(dp)
        return dp[-1]