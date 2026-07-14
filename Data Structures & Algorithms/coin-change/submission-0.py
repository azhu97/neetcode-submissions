class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if coin > i:
                    dp[i] = dp[i]
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[len(dp) - 1] == float('inf'):
            return -1
        return dp[len(dp) - 1]
        
            