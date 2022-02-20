from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_bananas = sum(piles)

        # the most inefficient distribution of piles is [1, 1, 1, 1, max_max_pile], so the biggest size possible is:
        max_max_pile = total_bananas - (len(piles) - 1)
        
        # the hours left to eat this pile:
        hours_left_to_eat_biggest_pile = h - (len(piles) - 1)
        
        # minimum speed (assuming all piles except one are always eaten with no remainder)
        min_speed = ceil(total_bananas/h)
        # maximum speed needed to eat hypothetical biggest pile in the hours left calculated previously,
        # much better estimator than max(piles)
        max_speed = ceil(max_max_pile/hours_left_to_eat_biggest_pile) 
        
        # regular binary search
        while min_speed <= max_speed:
            speed = (min_speed + max_speed) >> 1
            # sum(generator) does more work than regular for loop, as does not break early, but is faster 
            hours_needed = sum(ceil(pile / speed) for pile in piles)   
            # if hours needed to eat piles is too large, increase minimum eating speed to current speed + 1
            if hours_needed > h:
                min_speed = speed + 1
            else:
                # else decrease maximum eating speed to current speed - 1
                max_speed = speed - 1
            
        return min_speed

S = Solution()
S.minEatingSpeed([3,6,7,11], 8)