import bisect


class Solution:
    def findRightInterval(self, intervals):
        # sort with attached indexesinf is default if nothing is bigger, so then -1 is returned
        starts = sorted([interval[0], i] for i, interval in enumerate(intervals)) + [[float('inf'), -1]] 
        # run binary search of interval ends, in the starts list. return list of indexes in start that match 
        return [starts[bisect.bisect(starts, [interval[1]])][1] for interval in intervals]
