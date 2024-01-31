"""
Given an array of integers temperatures represents the daily temperatures,
return an arrayanswersuch thatanswer[i]is the number of days you have to wait
after theithday to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        # keep a monotonic stack of indexes of decreasing temperatures
        stack: list[int] = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res
