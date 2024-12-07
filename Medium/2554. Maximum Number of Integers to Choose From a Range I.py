"""
You are given an integer array banned and two integers n and maxSum. You are
choosing some number of integers following the below rules:
- The chosen integers have to be in the range [1, n].
- Each integer can be chosen at most once.
- The chosen integers should not be in the array banned.
- The sum of the chosen integers should not exceed maxSum.

Return the maximum number of integers you can choose following the mentioned rules.

Constraints:
- 1 <= banned.length <= 10^4
- 1 <= banned[i], n <= 10^4
- 1 <= maxSum <= 10^9
"""


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        """
        Complexity:
            Time: O(n + m)
            Space: O(1)
        """
        banned_set = set(banned)
        remaining = maxSum
        res = 0
        for i in range(1, n + 1):
            if i > remaining:
                break
            if i in banned_set:
                continue
            remaining -= i
            res += 1
        return res
