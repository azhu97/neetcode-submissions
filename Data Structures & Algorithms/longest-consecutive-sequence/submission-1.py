class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a hashmap to keep track of ordering 
        s = set(nums)
        res = 0
        for num in s:
            length = 1
            if (num - 1) not in s:
                while num + length in s:
                    length += 1
            res = max(res, length)

        return res
        
        