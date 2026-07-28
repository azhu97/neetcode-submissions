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
                if s[i - 1] not in first_set:
                    print("early")
                    return 0
                print(s[i - 1] not in first_set)
                dp[i] = dp[i - 1] if s[i - 1] in first_set else dp[i - 2]
            else:
                # s[i] != '0'
                # coupel scenarios
                # if s[i - 1] is 1 or 2, dp[i] = dp[i - 1] + 1
                # else if s[i - 1] is literally anything else, dp[i] = dp[i - 1]
                dp[i] = dp[i - 1]
                # decode is as s[i-1]s[i]
                
                if (s[i - 1] in first_set and s[i] not in second_set) or s[i - 1] == '1':
                    dp[i] += dp[i - 2] if i - 2 >= 0 else 1
        
        print(dp)
        return dp[-1]