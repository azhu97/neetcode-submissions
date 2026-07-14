class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(i, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            arr.append(nums[i])
            rec(i, total + nums[i], arr)
            arr.pop()
            rec(i + 1, total, arr)
        
        rec(0, 0, [])
        return res
            
        