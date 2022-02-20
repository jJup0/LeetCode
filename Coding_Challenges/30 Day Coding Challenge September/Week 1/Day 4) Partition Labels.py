from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> [int]:
        letterDict = defaultdict(list)
        for i, c in enumerate(S):
            letterDict[c].append(i)
        ranges = sorted([[indices[0], indices[-1]] for indices in letterDict.values()])
        i = 1
        while i < len(ranges):
            if ranges[i][0] < ranges[i-1][1]:
                ranges[i-1][1] = max(ranges[i-1][1], ranges[i][1])
                del ranges[i]
            else:
                i += 1
        return [r[1]-r[0] + 1 for r in ranges]
