# Definition for an interval.
import heapq
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals=sorted(intervals,key=lambda x:x.start)
        heap=list()
        for i in intervals:
            if (not heap) or i.start<heap[0]:
                heapq.heappush(heap,i.end)
            else:
                heapq.heapreplace(heap,i.end)
        return len(heap)





[[9,10],[4,9],[4,17],[6,8],[1,9]]
a=Interval(9,10)
b=Interval(4,9)
c=Interval(9,17)
d=Interval(9,11)
e=Interval(1,9)
intervals=[a,b,c,d,e]
sol=Solution()
print(sol.minMeetingRooms(intervals))


