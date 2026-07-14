class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            num = abs(num)
            if nums[num - 1] < 0:
                return num
            nums[num - 1] *= -1
        print(25)
