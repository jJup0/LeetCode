from typing import List


class Solution:
    """
    You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and
    verticalCuts where:
        horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal
        cut and similarly, and
        verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
    Return the maximum area of a piece of cake after you cut at each horizontal and vertical position
    provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number,
    return this modulo 10^9 + 7.
    Constraints:
        2 <= h, w <= 10^9
        1 <= horizontalCuts.length <= min(h - 1, 10^5)
        1 <= verticalCuts.length <= min(w - 1, 10^5)
        1 <= horizontalCuts[i] < h
        1 <= verticalCuts[i] < w
        All the elements in horizontalCuts are distinct.
        All the elements in verticalCuts are distinct.
    """

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        n = len(horizontalCuts), m = len(verticalCuts)
        O(n * log(n) + m * log(m)) Time
        """

        # sort cuts, so can iterate in order
        horizontalCuts.sort()
        verticalCuts.sort()

        # find the biggest width in cake slices
        biggest_width = 0
        cut = prev_cut = 0
        for cut in verticalCuts:
            size = cut - prev_cut
            if size > biggest_width:
                biggest_width = size
            prev_cut = cut

        # make imaginary slice at the end of the cake
        biggest_width = max(biggest_width, w - cut)

        # find the biggest height in cake slices
        biggest_height = 0
        cut = prev_cut = 0
        for cut in horizontalCuts:
            size = cut - prev_cut
            if size > biggest_height:
                biggest_height = size
            prev_cut = cut

        # make imaginary slice at the end of the cake
        biggest_height = max(biggest_height, h - cut)

        # multiply to get area, take modulo 10^9 + 7 like specified
        return (biggest_width * biggest_height) % 1000000007
