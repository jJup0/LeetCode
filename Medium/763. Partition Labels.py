class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        Create intervals of first and last occurance of characters
        and merge overlapping intervals.

        Complexity:
            x := unique characters in string length of alphabet
            Time: O(n * x) (O(n) is easily possible, but inputs are so small it does not matter)
            Space: O(x)
        """
        intervals = sorted((s.find(char), s.rfind(char)) for char in set(s))
        prev_start, prev_end = intervals[0]
        res: list[int] = []
        for start, stop in intervals:
            if stop < prev_end:
                continue
            if start > prev_end:
                res.append(prev_end - prev_start + 1)
                prev_start = start
            prev_end = stop

        res.append(prev_end - prev_start + 1)
        return res
