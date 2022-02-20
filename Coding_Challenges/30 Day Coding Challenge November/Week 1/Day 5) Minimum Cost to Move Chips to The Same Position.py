class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        for n in position:
            odd += n % 2
        return min(odd, len(position) - odd)
