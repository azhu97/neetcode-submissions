class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = [intervals[0]]
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < res[-1][1]:
                continue
            res.append(intervals[i])
        return len(intervals) - len(res)