"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        # min_heap = []

        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, interval.end)

        # return len(min_heap)
        d = defaultdict(int)
        for i in intervals:
            d[i.start]+=1
            d[i.end]-=1

        room=0
        ans=0
        for key in sorted(d.keys()):
            room+=d[key]
            ans=max(ans,room)
        return ans



        