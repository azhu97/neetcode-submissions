"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # have to think about this as a timeline 
        start = [tup.start for tup in intervals]
        start.sort()
        end = [tup.end for tup in intervals]
        end.sort()

        res = 0
        count = 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] <= end[e]:
                count += 1
                res = max(res, count)
                s += 1
            else:
                count -= 1
                e += 1
        
        return res