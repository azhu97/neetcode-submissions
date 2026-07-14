"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prevL, prevH = -1, -1 

        for t in intervals:
            tempL, tempH = t.start, t.end
            if tempL < prevH:
                return False
            prevL, prevH = tempL, tempH
        
        return True
            