class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        cellCycle = []
        for _ in range(min(N, 14)):
            newState = [0] * len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    newState[i] = 1
            cellCycle.append(newState)
            cells = newState
        return cellCycle[(N-1) % 14]
