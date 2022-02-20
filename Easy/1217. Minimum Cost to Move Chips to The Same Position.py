class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd  = sum(n & 1 for n in position) # same as n % 2
        return min(odd, len(position) - odd)