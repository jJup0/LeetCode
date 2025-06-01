"""
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such
that no child gets more than limit candies.

Constraints:
- 1 <= n <= 10^6
- 1 <= limit <= 10^6
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return self.distribute_candies_math_constant_time(n, limit)

    def distributeCandies_linear(self, n: int, limit: int) -> int:
        """
        Give most candies possibe to child1, add all distributions of child2 and
        child3 to result. Then take one candy from child1, give it to child2 if
        it does not have limit candies, else to child3 and repeat until child1
        has 0 candies or child2 and child3 have limit candies.

        Complexity:
            Time: O(n + limit)
            Space: O(1)
        """
        # edge case, there are too many candies
        if n > 3 * limit:
            return 0

        # initial distribution of candies to children, give as many as possible to child1, then child2
        child1 = min(n, limit)
        child2 = min(n - child1, limit)
        child3 = n - child1 - child2

        total_ways = 0
        for child1 in range(child1, -1, -1):
            # add to result ways that child2 can give child3 candies
            total_ways += child2 - child3 + 1
            # take a candy from child1 and give it to one of the others, if possible
            if child2 < limit:
                child2 += 1
            elif child3 < limit:
                child3 += 1
            else:
                break

        return total_ways

    def distribute_candies_math_constant_time(self, n: int, limit: int) -> int:
        """Based on the method above, mathematical solution in constant time."""
        if n > 3 * limit:
            return 0

        # initial distribution of candies to children, give as many as possible to child1, then child2
        child1 = min(n, limit)
        child2 = min(n - child1, limit)
        child3 = n - child1 - child2

        # first sum over range for giving candies from child1 to child2
        child2_after_getting_from_child1_max = child1
        range1_start = child2 - child3 + 1
        range1_end = child2_after_getting_from_child1_max - child3 + 1

        # then sum over range for giving candies from child1 to child3
        child1_after_giving_to_child2_max = child1 - (child1 - child2)
        max_for_child3 = min(limit, child3 + child1_after_giving_to_child2_max)
        range2_start = child2_after_getting_from_child1_max - max_for_child3 + 1
        # do not +1 here as it is already included in the sum above
        range2_end = child2_after_getting_from_child1_max - child3

        def range_sum(i: int, j_inclusive: int) -> int:
            return (j_inclusive + 1 - i) * (i + j_inclusive) // 2

        return range_sum(range1_start, range1_end) + range_sum(range2_start, range2_end)


def test():
    sol = Solution()
    res = sol.distributeCandies(3, 3)
    print(res)
    assert res == 10
    res = sol.distributeCandies(3, 4)
    print(res)
    assert res == 10


test()
