"""
You have k bags. You are given a 0-indexed integer array weights where
weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:
- No bag is empty.
- If the ith marble and jth marble are in a bag, then all marbles with an index
  between the ith and jth indices should also be in that same bag.
- If a bag consists of all the marbles with an index from i to j inclusively,
  then the cost of the bag is weights[i] + weights[j].

The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble
distributions.

Constraints:
- 1 <= k <= weights.length <= 10^5
- 1 <= weights[i] <= 10^9
"""

import itertools


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        """
        Important realization that by splitting the weights into intervals,
        the number to the left and right of each split are included in the
        score we can just find the k best/worst split indices.
        First and and last value in weights will always be included in
        score.

        Complexity:
            Time: O(n * log(n))
            Time: O(n)
        """
        if k == 1:
            return 0
        scores = sorted(val1 + val2 for val1, val2 in itertools.pairwise(weights))

        # both scores would include weights[0] + weights[-1] but since
        # we only care about the difference we can ignore this
        max_score = sum(scores[-k + 1 :])
        min_score = sum(scores[: k - 1])
        return max_score - min_score
