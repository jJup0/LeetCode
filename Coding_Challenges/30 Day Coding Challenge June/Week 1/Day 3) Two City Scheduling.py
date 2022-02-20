class orgSolution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        costs.sort(key=lambda x: abs(x[1]-x[0]), reverse=True)
        totA, totB, retVal = 0, 0, 0
        onlyTake = None
        for costA, costB in costs:
            if ((costA < costB) or onlyTake == 0) and onlyTake != 1:
                totA += 1
                retVal += costA
            else:
                totB += 1
                retVal += costB
            if totA >= len(costs)//2:
                onlyTake = 1
            if totB >= len(costs)//2:
                onlyTake = 0
        return retVal


class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        n = len(costs)
        retVal = 0
        for i in range(n//2):
            retVal += costs[i][0]
        for i in range(n//2, n):
            retVal += costs[i][1]
        return retVal
