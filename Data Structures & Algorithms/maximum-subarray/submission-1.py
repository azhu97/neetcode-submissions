class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = total = float('-inf')
        for num in nums:
            if total < 0:
                total = 0
            total += num 
            res = max(res, total)
        return res
        