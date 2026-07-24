class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # subarray is a contigious value
        # can we be greedy? no particular since negative * negative = positive
        # let dp[i] = (smallest, largest) including i
        dp = [(1, 1) for i in range(len(nums))]
        res = nums[0]
        dp[0] = (nums[0], nums[0])
        for i in range(1, len(nums)):
            prev_min, prev_max = dp[i - 1]
            # possiblities for dp[i]
            # 1. nums[i] 
            # 2. nums[i] * prev_min
            # 3. nums[i] * prev_max
            dp[i] = (min(nums[i], nums[i] * prev_min, nums[i] * prev_max), max(nums[i], nums[i] * prev_min, nums[i] * prev_max))
            res = max(res, dp[i][1])

        print(dp)
        return res