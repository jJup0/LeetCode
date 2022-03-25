from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort costs by difference of a and b
        costs.sort(key=lambda x: x[0]-x[1])
        
        # assuming len(costs) == 2n like in the specification
        n = len(costs) // 2
        
        # first half of people all fly to a, second all fly to b
        # minimum cost since sorted by difference in costs
        return sum(cost_a for cost_a, _ in costs[:n]) + sum(cost_b for _, cost_b in costs[n:])
     