from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use a sliding window, lower and upper bound, and store heights for efficiency
        lowerb = 0
        lowerb_height = height[lowerb]

        upperb = len(height) - 1
        upperb_height = height[upperb]

        res = 0
        # while sliding window has volume
        while lowerb < upperb:
            # calculate volume of current sliding window
            volume = (upperb - lowerb) * min(lowerb_height, upperb_height)
            # if it is the largest one so far, set it as the result
            if (volume > res):
                res = volume

            # greedily change the sliding window so that the next volume is maximized
            if lowerb_height < upperb_height:
                lowerb += 1
                lowerb_height = height[lowerb]
            else:
                upperb -= 1
                upperb_height[upperb]

        return res
