class Solution:
    def nthUglyNumber(self, n):
        factors, k = [2, 3, 5], 3
        timesused, uglyNumbers = [0, 0, 0], [1]
        for i in range(n-1):
            candidates = [factors[i]*uglyNumbers[timesused[i]] for i in range(k)]
            new_num = min(candidates)
            uglyNumbers.append(new_num)
            timesused = [timesused[i] + (candidates[i] == new_num) for i in range(k)]
        return uglyNumbers[-1]
