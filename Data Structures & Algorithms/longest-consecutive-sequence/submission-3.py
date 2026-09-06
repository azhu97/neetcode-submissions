from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # easy way to do it
        # nums -> set -> sort set -> window it
        # nlogn runtime 
        s = set(nums)
        res = 1
        for num in s:
            if num - 1 in s:
                continue
            temp = 1
            while num + temp in s:
                temp += 1
            res = max(res, temp)
        return res
        