from collections import deque


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> [int]:
        deltas = [-K, K] if K > 0 else [K]

        results = deque(range(10))
        threshold = 10**(N-1) if N > 1 else 0

        while results[0] < threshold:
            n = results.popleft()
            if n == 0:
                continue

            digit = n % 10
            for delta in deltas:
                if 0 <= digit + delta <= 9:
                    results.append(n*10 + digit + delta)

        return results
