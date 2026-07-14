class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        factor = nums[0]
        for i in range(1, len(nums)):
            res[i] *= factor
            factor *= nums[i]
        print(res)
        factor = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= factor
            factor *= nums[i]
        print(res)

        return res
        
