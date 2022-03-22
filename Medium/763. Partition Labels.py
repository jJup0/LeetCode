from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ord_a = ord('a')

        # store first and last occurances of letters
        # using lists instead of dicts makes zipping easier, also they have fixed size of 26 due to:
        # constraint: s consists of lowercase English letters.
        starts = [-1] * 26
        ends = [-1] * 26

        # find first and last occurances of letters
        for i, c in enumerate(s):
            # index in the starts/ends list is ord(c) - ord('a')
            ord_c_standard = ord(c) - ord_a
            if starts[ord_c_standard] == -1:
                starts[ord_c_standard] = ends[ord_c_standard] = i
            else:
                ends[ord_c_standard] = i

        # interval lenght lists
        res = []

        # start and end of "ongoing" interval
        prev_start = prev_end = -1

        # sort intervals, to find overlaps easily
        for start, end in sorted(interval for interval in zip(starts, ends)):
            # if start == -1, the letter was not present so there is no interval
            if start == -1:
                continue

            # intervals overlap exactly when the start is before the current end of the
            # ongoing interval, to to the intervals being sorted
            if start < prev_end:
                # extend the ongoing interval end index if necessary
                prev_end = max(prev_end, end)
            else:
                # if ongoing interval is not the pseudo one defined at the start, add its
                # length to the result list
                if prev_end != -1:
                    res.append(prev_end - prev_start + 1)

                # reset ongoing interval start and end
                prev_start = start
                prev_end = end

        # add any interval that was still ongoing
        # due to constraint: 1 <= s.length, this will never be the pseudo interval (-1,-1)
        res.append(prev_end - prev_start + 1)

        return res
