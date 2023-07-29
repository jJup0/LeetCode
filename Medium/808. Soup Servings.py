from functools import cache


class Solution:
    """
    There are two types of soup: type A and type B. Initially, we have n ml of
    each type of soup. There are four kinds of operations:

    1. Serve 100 ml of soup A and 0 ml of soup B,
    2. Serve 75 ml of soup A and 25 ml of soup B,
    3. Serve 50 ml of soup A and 50 ml of soup B, and
    4. Serve 25 ml of soup A and 75 ml of soup B.

    When we serve some soup, we give it to someone, and we no longer have it.
    Each turn, we will choose from the four operations with an equal probability
    0.25. If the remaining volume of soup is not enough to complete the operation,
    we will serve as much as possible. We stop once we no longer have some
    quantity of both types of soup.

    Note that we do not have an operation where all 100 ml's of soup B are used first.

    Return the probability that soup A will be empty first, plus half the
    probability that A and B become empty at the same time. Answers within 10-5
    of the actual answer will be accepted.

    Constraints:
    - 0 <= n <= 10^9
    """

    def soupServings(self, n: int) -> float:
        """
        O(1) / O(1)     time / space complexity
        """
        if n >= 5000:
            # n is large enough so that rounded to 5 decimal places the result is 1
            return 1

        @cache
        def prob(a_remaining: int, b_remaining: int) -> float:
            if a_remaining <= 0:
                if b_remaining <= 0:
                    # both are empty at the same time
                    return 0.5
                # a is empty first
                return 1
            if b_remaining <= 0:
                # b is empty first,
                return 0

            # return sum of probabilities for different possibilities of serving soup
            return (
                sum(
                    prob(a_remaining - remove_a, b_remaining - 100 + remove_a)
                    for remove_a in range(100, 24, -25)
                )
                * 0.25
            )

        return prob(n, n)
