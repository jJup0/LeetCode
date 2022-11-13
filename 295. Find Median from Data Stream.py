import bisect
from collections import deque

from test_data_generator import ComplexStructureTestData


class MedianFinder:

    def __init__(self):
        self.allNums = []
        self.deque = deque()

    def addNum(self, num: int) -> None:
        if not self.deque:
            bisect.insort(self.allNums, num)
            self.deque.append(num)
        else:
            if num <= self.deque[0]:
                bisect.insort(self.allNums, num)
                self.deque.appendleft(num)
            elif num >= self.deque[-1]:
                bisect.insort(self.allNums, num)
                self.deque.append(num)
            else:
                self.deque.popleft()
                self.deque.pop()
                self.addNum(num)

    def findMedian(self) -> float:
        res = sum(self.deque) / len(self.deque)
        real_median = (self.allNums[len(self.allNums) // 2] + self.allNums[(len(self.allNums) -1) // 2]) / 2
        print(real_median, res, self.allNums, self.deque)
        return res


S = MedianFinder()
import random

random.seed(0)
nums = [random.randint(0, 100) for _ in range(10)]
print(nums)
for num in nums:
    S.addNum(num)
    S.findMedian()

if 0:
    S = None
    td = ComplexStructureTestData()
    methods, paramss = td.median_from_data_stream(100)
    print(methods, paramss)
    for method, params in zip(methods, paramss):
        if method == "MedianFinder":
            S = MedianFinder(*params)
        else:
            res = eval(f"S.{method}({','.join(str(param) for param in params)})")
            # if res:
            # print(res)
