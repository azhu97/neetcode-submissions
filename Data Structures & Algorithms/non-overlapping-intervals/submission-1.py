class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            # case that we have to remove
            # 1. interval[0] < prev_end
            # in this case, we have to remove atleast one, so we remove the the larger one for greed sake
            if interval[0] < prev_end:
                print(prev_end, interval)
                prev_end = min(prev_end, interval[1])
                res += 1
            else:
                # means there is no merge
                prev_end = interval[1]
        
        return res