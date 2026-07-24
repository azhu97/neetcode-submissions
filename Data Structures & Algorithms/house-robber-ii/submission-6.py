class Solution:
    def rob(self, nums: List[int]) -> int:
        # you are given nums
        # nums[i] = amount of money of the ith house 
        # arranged in a circle -> first and last house are neighbors
        # you cannot rob two adj. houses
        # let dp[i] = max amount of money after passing dp[i]
        # dp[0] should = nums[0]
        # if you are doing it dp, you have to think, what is the best course of action at each house 
        # 1. choose to rob the house -> nums[i] + dp[i - 2]
        # 2. choose not to rob the house -> dp[i - 1]
        # since this is a house, we can choose to rob either the first house or rob the second hosue
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        res = float('-inf')
        
        # forward route 
        for i, money in enumerate(nums):
            if i == 0 or i == len(nums) - 1:
                continue
            dp[i] = max(dp[i - 1], (dp[i - 2] if i - 2 >= 0 else 0) + money)
            res = max(res, dp[i])
        print(dp) 
        # backward route
        dp[-1] = nums[-1]
        for i in range(len(nums) - 1, -1 , -1):
            if i == 0 or i == len(nums) - 1:
                continue
            dp[i] = max(dp[i + 1], (dp[i + 2] if i + 2 < len(nums) else 0) + nums[i])
            res = max(res, dp[i])
        print(dp)
        print(res)
        
        