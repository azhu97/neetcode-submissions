"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = [] # contains (start, end) of rooms
        # n + nlogn = n
        res = 1
        print(intervals[0])
        heapq.heappush(heap, (intervals[0].start, intervals[0].end))
        # what scenario would we increase this
        # we look at each room
        # we add to the heap each time
        # we want to see if
        for interval in intervals[1::]:
            while heap:
                prev_start, prev_end = heapq.heappop(heap)
                # if it conflicts, we have to make a new room
                if (interval.start) < prev_end:
                    res += 1
                    break

            heapq.heappush(heap, (interval.start, interval.end))

        return res
