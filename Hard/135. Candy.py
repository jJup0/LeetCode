from collections import defaultdict


class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    """

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

    def candy_two_pass(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # update from left to right, incrementing candies
        # if rating higher than previous
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # update from right to left, incrementing if rating higher than
        # next and current candies lower than next
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)
