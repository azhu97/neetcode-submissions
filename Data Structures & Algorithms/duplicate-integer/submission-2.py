class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = []
        for num in nums:
            if num in contains:
                return True
            contains.append(num)
        return False


         