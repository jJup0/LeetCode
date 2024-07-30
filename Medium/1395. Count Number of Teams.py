"""
There are n soldiers standing in a line. Each soldier is assigned a unique
rating value.

You have to form a team of 3 soldiers amongst them under the following rules:
- Choose 3 soldiers with index ( i, j, k ) with rating ( rating[i], rating[j],
  rating[k] ).
- A team is valid if: ( rating[i] < rating[j] < rating[k] ) or (
  rating[i] > rating[j] > rating[k] ) where ( 0 <= i < j < k < n ).

Return the number of teams you can form given the conditions. (soldiers can be
part of multiple teams).

Constraints:
- n == rating.length
- 3 <= n <= 1000
- 1 <= rating[i] <= 10^5
- All the integers in rating are unique.
"""


class Solution:
    def numTeams(self, ratings: list[int]) -> int:
        """
        O(n^2) / O(n)   time / space complexity
        """
        prevs: list[tuple[int, int, int]] = []
        res = 0
        for rating in ratings:
            curr_inc_second = curr_dec_second = 0
            for prev_rating, inc_second, dec_second in prevs:
                if rating > prev_rating:
                    curr_inc_second += 1
                    res += inc_second
                else:
                    curr_dec_second += 1
                    res += dec_second

            prevs.append((rating, curr_inc_second, curr_dec_second))

        return res
