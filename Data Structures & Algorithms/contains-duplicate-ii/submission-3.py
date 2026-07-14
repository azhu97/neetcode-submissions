class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums = array of integers 
        # k = integer 
        # if i != j && nums[i] == nums[j] && abs(i - j) <= k
        # use a hashmap to keep the oldest
        mapping = {} # num : i 
        for i, num in enumerate(nums):
            if num in mapping and abs(mapping[num] - i) <= k:
                return True
            mapping[num] = i

        return False