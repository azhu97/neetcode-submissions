"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # given the intervals
        # find the min number of rooms required to schedule all rooms without conflict
        # the max number of rooms needed = len(intervals)
        # need to find a way to reduce this
        res = 0
        prev_end = float('inf')
        for interval in intervals:
            if interval.start < prev_end:
                prev_end = interval.end
                res += 1

        return res