class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            m = 1
            for b in range(i):
                if nums[i] > nums[b]:
                    m = max(m, dp[b] + 1)
            dp[i] = m
        
        m = 0
        for num in dp:
            m = max(m, num)
        return m  
        