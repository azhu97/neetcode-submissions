class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        for i, c in count_map.items():
            if c == 1:
                return i