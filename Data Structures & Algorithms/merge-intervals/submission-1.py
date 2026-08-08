class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort all arrays
        # then just merge them if they overlap
        intervals.sort()
        res = [] 
        for start, end in intervals:
            if len(res) == 0 or start > res[-1][1]:
                res.append([start, end])
                continue
            res[-1][1] = max(res[-1][1], end)
        
        return res