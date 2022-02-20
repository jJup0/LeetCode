from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = last_taken = i = seats.index(1)
        n = len(seats)
        while i < n:
            if seats[i]:
                dist = (i - last_taken) >> 1
                if dist > res:
                    res = dist
                last_taken = i
            i += 1
        
        return max(res, n - last_taken - 1)