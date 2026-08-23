class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        print(f"half: {half}")
        # think of it as a knapsack problem, 
        # think of dp = [False * (half + 1)] where dp[0] = True
        # dp[i] = True if we can make total i with numbers in nums
        dp = [False for i in range(half + 1)]
        dp[0] = True
        for num in nums:
            for i in range(1, len(dp)):
                if dp[i]:
                    continue
                if i - num >= 0:
                    dp[i] = dp[i] or dp[i - num]
        print(dp[-1])
        return dp[-1]