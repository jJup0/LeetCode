from collections import defaultdict


class mySolution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)
        interval_len_dict = defaultdict(list)
        for start, end in intervals:
            interval_len_dict[end-start].append((start, end))
        interval_lens = sorted(interval_len_dict.keys(), reverse=True)
        for larger_idx, larger_range in enumerate(interval_lens):
            for starti, endi in interval_len_dict[larger_range]:
                for smaller_idx, smaller_range in enumerate(interval_lens[larger_idx + 1:]):
                    j = 0
                    while j < len(interval_len_dict[smaller_range]):
                        startj, endj = interval_len_dict[smaller_range][j]
                        if starti <= startj and endi >= endj:
                            res -= 1
                            interval_len_dict[smaller_range].remove((startj, endj))
                        else:
                            j += 1

        return res


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = 1
        start = intervals[0][0]
        prev_end = intervals[0][1]

        for new_start, new_end in intervals:
            if start == new_start:
                prev_end = new_end
            elif prev_end <= new_start or prev_end < new_end:
                res += 1
                prev_end = new_end

        return res
