"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        end = sorted(j.end for j in intervals)
        i = 0
        j = 0
        rooms = 0
        res = 0
        while i < len(intervals):
            if starts[i] < end[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1

            res = max(res, rooms)
        return res
