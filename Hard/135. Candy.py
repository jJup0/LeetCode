from collections import defaultdict
from typing import List


class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive
    elements sequence.
    You must write an algorithm that runs in O(n) time.
    Constraints:
        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """

    def candy(self, ratings: List[int]) -> int:
        """
        Greedily assign lowest candies possible to children with lowest rating.
        O(n) / O(n)     time/space complexity
        """

        # store (incremented) indexes of each rating
        rating_index_map = defaultdict(list)
        for i, rating in enumerate(ratings, start=1):
            rating_index_map[rating].append(i)

        # candies[i+1] stores how many candies need to be given to child[i]
        # (use padded array to avoid checking if i==0 or i==n-1)
        candies = [0] * (len(ratings) + 2)

        # go through ratings in increasing order
        for rating, idxs in sorted(rating_index_map.items()):
            # iterating through ratings in ascending order means that candies required for at i is
            # max(neighbors_candies) + 1. Have to store in temporary array, because neighboring
            # indexes with the same rating can have the same amount of candy
            to_insert = [max(candies[idx-1], candies[idx+1]) + 1 for idx in idxs]

            # update candies
            for j, idx in enumerate(idxs):
                candies[idx] = to_insert[j]

        # return sum of candies needed
        return sum(candies)
