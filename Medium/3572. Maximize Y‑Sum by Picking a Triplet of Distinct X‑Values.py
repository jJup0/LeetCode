"""
You are given two integer arrays x and y, each of length n. You must choose
three distinct indices i, j, and k such that:
- x[i]!= x[j]
- x[j]!= x[k]
- x[k]!= x[i]

Your goal is to maximize the value of y[i] + y[j] + y[k] under these
conditions. Return the maximum possible sum that can be obtained by choosing
such a triplet of indices.

If no such triplet exists, return -1.

Constraints:
- n == x.length == y.length
- 3 <= n <= 10^5
- 1 <= x[i], y[i] <= 10^6
"""

MOD = 10**9 + 7


class Solution:
    def maxSumDistinctTriplet(self, x: list[int], y: list[int]) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        ys = sorted(((num, i) for i, num in enumerate(y)), reverse=True)
        # values in x current being used for bigest triplet
        biggest_x_vals: list[int] = []
        y_triplet: list[int] = []
        for num, i in ys:
            # if value in x is already in use, continue
            if x[i] in biggest_x_vals:
                continue
            # otherwise use the current y-value in triplet
            y_triplet.append(num)
            biggest_x_vals.append(x[i])
            if len(y_triplet) == 3:
                # triplet is full, we can break
                break
        if len(y_triplet) < 3:
            # there are less than 3 unique numbers in x, no triplet can be formed
            return -1
        return sum(y_triplet)


def test():
    s = Solution()
    res = s.maxSumDistinctTriplet([1, 2, 1, 3, 2], [5, 3, 4, 6, 2])
    real = 14
    assert res == real, res


test()
