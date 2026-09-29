class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2d dp, similar to knapsack
        # let dp be len(nums) + 1 * target * 2 + 1 to represent negative and positive
        # let dp[i][j] = represent the number of ways to represent j - (target // 2) 
        total = sum(nums)
        dp = [[0 for j in range(total * 2 + 1)] for i in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                value = nums[i - 1]
                # can you add to this value
                if j - value >= 0:
                    dp[i][j] += dp[i - 1][j - value]
                if j + value <= len(dp[0]) - 1:
                    dp[i][j] += dp[i - 1][j + value]
        for d in dp: print(d)
        return dp[-1][len(dp[0]) // 2 + target]