class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # find the missing number in nums
        # [1, 2, 3] = [0001, 0010, 0011], missing number 0 -> 0000
        # [0, 2] = [0000, 00010], missing number 1 -> 0001
        # [1] = [0001], missing 0 -> 0000
        # [0] = [0000], missing 1 -> 0001
        target = 0
        for i in range(1, len(nums) + 1):
            target ^= i
        for num in nums:
            target ^= num
        return target
            