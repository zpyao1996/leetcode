# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda v: v.start)
        new_intervals = []
        last_left = intervals[0].start
        last_right = intervals[0].end
        for interval in intervals:
            cur_left, cur_right = interval.start, interval.end
            if cur_left <= last_right:
                last_right = max(last_right, cur_right)
            else:
                new_intervals.append(Interval(last_left, last_right))
                last_left, last_right = cur_left, cur_right
        new_intervals.append(Interval(last_left, last_right))
        return new_intervals