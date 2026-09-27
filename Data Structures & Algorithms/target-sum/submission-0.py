class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for each num in arr, either add it or subtract is to a total sum
        # return the number of ways we build the expression
        # this is similar to a knapsack problem
        # we let dp[len(nums) + 1][target + 1],
        # where dp[i][j] represents the number of ways to reach value j, given the first i items
        # base case -> dp[0][0] = 1, don't include anything
        # leave everything else 0
        total_sum = sum(nums)
        dp = [[0 for j in range(total_sum + 1)] for i in range(len(nums) + 1)]
        dp[0][0] = 1
        for d in dp: print(d)
        print("1")
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0: continue
                value = nums[i - 1] 
                # we have two options
                # 1. we add the number -> dp[i][j] += dp[i - 1][j - value]
                # 2. we subtract -> dp[i][j - value] += dp[i][j]
                if j - value >= 0:
                    dp[i][j] += dp[i - 1][j - value]
                    dp[i][j - value] += dp[i][j]
                # for each of these, we should should check bounds of what we are trying to dp

        for d in dp: print(d)