from math import ceil


class Solution:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
    The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of
    bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all
    of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards
    return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

    Constraints:
        1 <= piles.length <= 10^4
        piles.length <= h <= 10^9
        1 <= piles[i] <= 10^9
    """

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Binary search for minimum speed needed.
        O(n * log(n)) / O(1)    time / space complexity
        """
        total_bananas = sum(piles)

        # lower bound for eating speed: piles are virtually perfectly distributed,
        # i.e. sum(abs(h - (pile % h)) for pile in piles) < h
        min_speed = ceil(total_bananas/h)

        # the most inefficient distribution (requiring highest speed) of piles is
        # [1, 1, 1, ..., max_max_pile], so the biggest pile possible is:
        max_max_pile = total_bananas - (len(piles) - 1)

        # the hours left to eat this largest pile:
        hours_remaining_to_eat_biggest_pile = h - (len(piles) - 1)

        # upper bound for speed is speed needed to east needed to eat
        # hypothetical biggest pile in the hours remaining
        max_speed = ceil(max_max_pile/hours_remaining_to_eat_biggest_pile)

        # regular binary search
        while min_speed <= max_speed:
            speed = (min_speed + max_speed) >> 1

            # sum(generator) does more work than regular for loop, as does not break early, but is faster
            hours_needed = sum(ceil(pile / speed) for pile in piles)

            if hours_needed > h:
                # if hours needed to eat piles is too large, increase minimum eating speed to current speed + 1
                min_speed = speed + 1
            else:
                # else decrease maximum eating speed to current speed - 1
                max_speed = speed - 1

        return min_speed
