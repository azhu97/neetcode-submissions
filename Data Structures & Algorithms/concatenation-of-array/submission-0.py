class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(2):
            for num in nums:
                arr.append(num)
        return arr
        