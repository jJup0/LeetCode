"""
There is a circle of red and blue tiles. You are given an array of integers
colors and an integer k. The color of tile i is represented by colors[i]:
- colors[i] == 0 means that tile i is red.
- colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating
colors (each tile in the group except the first and last one has a different
color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are
considered to be next to each other.

Constraints:
- 3 <= colors.length <= 10^5
- 0 <= colors[i] <= 1
- 3 <= k <= colors.length
"""


class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        alt_count = [0] * len(colors)
        # calculate streaks for alternating colors
        for i, col in enumerate(colors):
            if col != colors[i - 1]:
                alt_count[i] = alt_count[i - 1] + 1
            else:
                alt_count[i] = 1

        # do it again with the streaks for the last color set
        for i, col in enumerate(colors):
            if col != colors[i - 1]:
                alt_count[i] = alt_count[i - 1] + 1
            else:
                # optimiziation to avoid unecessary work
                break

        return sum(streak >= k for streak in alt_count)
