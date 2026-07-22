class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we should just do a running max jump 
        res = nums[0]
        for i, jump in enumerate(nums):
            if i == 0 or i > res:
                continue
            res = max(res, i + jump)
        print(res)
        return res >= len(nums) - 1