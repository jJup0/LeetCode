from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        # there are only two candidates so that all of the tops or bottoms can be the same
        # which are the two values on the first domino, only track flips for one candidate
        cand = tops[0]
        alt_cand = bottoms[0]
        
        # for the other candidate only track if it has been present in every domino so far
        alt_cand_present = True
        
        # store the amount of switches needed for all the top to be the same, and all the 
        # bottom. switches_for_top != len(tops) - switches_for_bottom because dominoes can
        # have the same value on each side.
        switches_for_top = 0
        switches_for_bottom = 0

        # iterats through dominoes
        for top, bottom in zip(tops, bottoms):
            
            # check if candidate is present in domino
            missing_from_top = cand != top
            missing_from_bottom = cand != bottom
            
            # same for alternative candidate
            alt_cand_present = alt_cand_present and (alt_cand == top or alt_cand == bottom)

            # candidate not present in domino
            if missing_from_top and missing_from_bottom:
                # if candidate is missing, and alternative candidate is also no long valid return -1
                if not alt_cand_present:
                    return -1
                
                # if the alternative candidate has always been present so far, that means every 
                # domino until now has been (cand, alt_cand) or vice versa
                # so replace candidate with alternative
                cand = alt_cand
                
                # set alt_cand_present false since candidate is now alt_cand
                alt_cand_present = False
                
                # switch the amount of switches needed for top and bottom
                switches_for_top, switches_for_bottom = switches_for_bottom, switches_for_top
                
                # recalculate where candidate is missing (is definitely present)
                missing_from_top = cand != top
                missing_from_bottom = cand != bottom

            # if domino is missing from top, then it is present in the bottom, and a switch is required
            if missing_from_top:
                switches_for_top += 1
            elif missing_from_bottom:
                switches_for_bottom += 1

        return min(switches_for_top, switches_for_bottom)
