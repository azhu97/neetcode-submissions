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
        heapq.heappush(heap, (intervals[0].end))
        # what scenario would we increase this
        # we look at each room
        # we add to the heap each time
        # we want to see if
        for interval in intervals[1::]:
            # peak the top of the heap, and see if there is no conflict
            if interval.start < heap[0]:
                res += 1
            heapq.heappush(heap, interval.end)
        return res