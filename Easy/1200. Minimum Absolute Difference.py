from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        smallestDist = float('inf')
        prev = float('-inf')
        res = []
        for num in arr:
            diff = num - prev
            if diff < smallestDist:
                res = [(prev, num)]
                smallestDist = diff
            elif diff == smallestDist:
                res.append((prev, num))
            prev = num
        return res