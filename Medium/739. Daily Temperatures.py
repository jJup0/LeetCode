# import heapq
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #         # somewhat slow, no need for minheap, is in O(n*log(n))
        #         res = [0] * len(temperatures)
        #         # minheap to track lowest temperatures so far
        #         prevTemps = []
        #         for i in range(len(temperatures)):
        #             temp = temperatures[i]
        #             # print(temp, prevTemps)
        #             while prevTemps and prevTemps[0][0] < temp:
        #                 prevTemp, j = heapq.heappop(prevTemps)
        #                 res[j] = i-j
        #             heapq.heappush(prevTemps, (temp, i))
        #         # print(temperatures)
        #         # print(res)
        #         return res

        # keeps all indexs of days that havent had a warmer day
        stack = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res
