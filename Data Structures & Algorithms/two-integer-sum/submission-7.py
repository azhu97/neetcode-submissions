class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # greedy approach, must be sorted 
        cache = {}
        
        for i, num in enumerate(nums):
            look = target - num
            if look in cache:
                return [cache[look], i]
            cache[num] = i