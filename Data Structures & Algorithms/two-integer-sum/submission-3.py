class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapOfNumber = {}
        for i in range(len(nums)):
            otherNumber = target - nums[i];
            if otherNumber in mapOfNumber:
                value = [i, mapOfNumber[otherNumber]]
                value.sort()
                return value
            if nums[i] not in mapOfNumber:
                mapOfNumber[nums[i]] = i
            