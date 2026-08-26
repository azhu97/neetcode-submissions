class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # this is as simple as having a 1D array
        # work backwards, dp[0 for i in range(amount + 1)]
        # dp[0 for i in range(amount + 1)], dp[i] represents number of ways to make amount i
        # dp[0] = 1, only 1 way to make 1
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(1, len(dp)):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        
        return dp[-1]