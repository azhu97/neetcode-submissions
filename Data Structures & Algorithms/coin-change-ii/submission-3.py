class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins -> coins of different denominations 
        # amount -> target amount of money
        # return the number of ways of combination to total up amount
        # some sort of dp value
        # dp[len(coins) + 1][amount + 1], dp[i][j] = number of ways to make j including coin i again
        # dp[i][j] = add up everything on column j - coins[i]
        # return summations of the [-1] column
        # columns by column
        # base case = dp[0][0] = 1, the only way to make zero to include nothing
        # for every n (2n * a) = O(n*a)
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]
        dp[0][0] = 1
        for j in range(1, len(dp[0])):
            for i in range(1, len(dp)):
                coin = coins[i - 1]
                target = j - coin
                if target >= 0:
                    for y in range(len(dp)):
                        dp[i][j] += dp[y][target]
        res = 0 
        for arr in dp:
            #print(arr)
            res = max(res, arr[-1])
        return res