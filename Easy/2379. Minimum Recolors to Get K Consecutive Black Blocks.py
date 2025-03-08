"""
You are given a 0-indexed string blocks of length n, where blocks[i] is
either 'W' or'B', representing the color of the ith block. The characters 'W'
and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive
black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one
occurrence of k consecutive black blocks.

Constraints:
- n == blocks.length
- 1 <= n <= 100
- blocks[i] is either 'W' or'B'.
- 1 <= k <= n
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """Sliding window approach - count white blocks in k-window.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        white_in_window = sum(blocks[i] == "W" for i in range(k))
        res = white_in_window
        for i in range(k, len(blocks)):
            white_in_window += blocks[i] == "W"
            white_in_window -= blocks[i - k] == "W"
            if white_in_window < res:
                res = white_in_window
        return res
