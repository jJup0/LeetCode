"""
There are n children standing in a line. Each child is assigned a rating value
given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies
to the children.

Constraints:
- n == ratings.length
- 1 <= n <= 2 * 10^4
- 0 <= ratings[i] <= 2 * 10^4
"""

from collections import defaultdict


class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Greedily assign lowest candies possible to children with lowest rating.
        O(n) / O(n)     time/space complexity
        """

        # store (incremented) indexes of each rating
        rating_index_map: defaultdict[int, list[int]] = defaultdict(list)
        for i, rating in enumerate(ratings, start=1):
            rating_index_map[rating].append(i)

        # candies[i+1] stores how many candies need to be given to child[i]
        # (use padded array to avoid checking if i==0 or i==n-1)
        candies = [0] * (len(ratings) + 2)

        # go through ratings in increasing order
        for rating, idxs in sorted(rating_index_map.items()):
            # iterating through ratings in ascending order means that candies
            # required for at i is max(neighbors_candies) + 1. The candy
            # assignments have to be stored in a temporary array, because
            # neighboring indexes with the same rating can have the same
            # amount of candy
            to_insert = [max(candies[idx - 1], candies[idx + 1]) + 1 for idx in idxs]

            # update candies
            for c, idx in enumerate(idxs):
                candies[idx] = to_insert[c]

        # return sum of candies needed
        return sum(candies)
