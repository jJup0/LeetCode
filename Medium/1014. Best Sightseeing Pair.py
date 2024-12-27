"""
You are given an integer array values where values[i] represents the value of
the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i
between them.

The score of a pair ( i < j ) of sightseeing spots is
values[i] + values[j] + i - j: the sum of the values of the sightseeing spots,
minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Constraints:
- 2 <= values.length <= 5 * 10^4
- 1 <= values[i] <= 1000
"""


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        return self.maxScoreSightseeingPair2(values)

    def maxScoreSightseeingPair2(self, values: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        largest_val = values[0]
        res = 0
        for j in range(1, len(values)):
            val = values[j]
            largest_val -= 1
            res = max(res, val + largest_val)
            if val > largest_val:
                largest_val = val
        return res

    def maxScoreSightseeingPair1(self, values: list[int]) -> int:
        """
        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        values_idx = sorted(((val, i) for i, val in enumerate(values)), reverse=True)
        res = 0
        for idx1, (val1, i) in enumerate(values_idx):
            if val1 * 2 - 1 <= res:
                break
            for idx2 in range(idx1 + 1, len(values_idx)):
                val2, j = values_idx[idx2]
                if val2 + val1 - 1 <= res:
                    break
                res = max(res, val1 + val2 - abs(j - i))
        return res
