import random
import bisect


class Solution:
    def __init__(self, rects: [[int]]):
        self.rects = rects
        self.weights = [0]
        for x1, y1, x2, y2 in rects:
            self.weights.append(((x2-x1+1) * (y2-y1+1)) + self.weights[-1])
        self.weights = self.weights[1:]

    def pick(self) -> [int]:
        val = random.randrange(self.weights[-1]) + 1
        lo = bisect.bisect_left(self.weights, val)
        x1, y1, x2, y2 = self.rects[lo]
        return [random.randint(x1, x2), random.randint(y1, y2)]
