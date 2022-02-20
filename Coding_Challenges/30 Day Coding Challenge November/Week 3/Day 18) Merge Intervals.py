class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.append([float('inf'), float('inf')])
        intervals.sort()
        currStart, currEnd = intervals[0]
        res = []
        for start, end in intervals:
            if currStart <= start <= currEnd:
                currEnd = max(currEnd, end)
            else:
                res.append((currStart, currEnd))
                currStart, currEnd = start, end
        res.append((currStart, currEnd))
        return res
