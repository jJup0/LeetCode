# NOT WORKING FOR TIME LIMIT, problem probably with visited
from collections import defaultdict
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        goal = len(arr) - 1
        if goal <= 1:
            return goal
        
        
        # true initialization would be range(0, goal + 1), but dfs would always go to base case for first visit
        dp = [i for i in range(1, goal + 2)]  
        
        stations = defaultdict(list)
        for i, num in enumerate(arr):
            stations[num].append(i)
        
        def dfs(pos, jumps):
            if jumps >= dp[pos]:
                return
            dp[pos] = jumps
            
            if pos == goal:
                return
            
            jumps += 1
            for new_pos in stations[arr[pos]]:
                if new_pos != pos:
                    dfs(new_pos, jumps)
            dfs(pos + 1, jumps)
            if pos:
                dfs(pos - 1, jumps)
            
                        
            
        dfs(0, 0)
        return dp[goal]

S = Solution()
x = S.minJumps([6,1,9])
print(x)