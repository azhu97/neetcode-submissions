class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # given non-overlapping intervals, intervals 
        # -> [start_i, end_i]
        intervals.append(newInterval)
        heapq.heapify(intervals)
        res = []
        print(intervals)
        while intervals:
            interval = heapq.heappop(intervals)
            if not res or interval[0] > res[-1][1]:
                # if the interval list is empty or they don't conflict, just add
                res.append(interval)
            else:
                # they overlap
                prev_interval = res.pop()
                new_interval = [min(prev_interval[0], interval[0]), max(prev_interval[1], interval[1])]
                res.append(new_interval)
        
        return res
