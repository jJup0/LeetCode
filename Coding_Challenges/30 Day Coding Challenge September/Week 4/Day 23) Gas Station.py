class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g - c for g, c in zip(gas, cost)]
        if sum(diffs) < 0:
            return -1
        for i in range(1, len(diffs)):
            diffs[i] += diffs[i - 1]
        return (diffs.index(min(diffs)) + 1) % len(diffs)

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         cur_gas = 0
#         minindex = 0
#         min_spare_gas = float('inf')
#         for i,d in enumerate(zip(gas,cost)):
#             cur_gas += d[0] - d[1]
#             if cur_gas < min_spare_gas:
#                 min_spare_gas = cur_gas
#                 minindex = i
#         if cur_gas < 0:
#             return -1
#         return (minindex + 1)%len(gas)
