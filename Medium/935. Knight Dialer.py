"""
The chess knight has a unique movement, it may move two squares vertically
and one square horizontally, or two squares horizontally and one square
vertically (with both forming the shape of an L). The possible movements
of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

https://assets.leetcode.com/uploads/2020/08/18/chess.jpg

We have a chess knight and a phone pad as shown below, the knight can only
stand on a numeric cell (i.e. blue cell).

https://assets.leetcode.com/uploads/2020/08/18/phone.jpg

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then
you should perform n - 1 jumps to dial a number of length n. All jumps
should be valid knight jumps.

As the answer may be very large, return the answer modulo 10^9 + 7.
"""


class Solution:
    def knightDialer(self, n: int) -> int:
        """
        Store amount of numbers ending in digit and simulate rounds.
        O(n) / O(1)     time / space complexity
        """
        MOD = 10**9 + 7
        digit_to_knight_neighbors = (
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (3, 9, 0),
            (),
            (1, 7, 0),
            (2, 6),
            (1, 3),
            (2, 4),
        )

        ways = [1] * 10
        for _ in range(n - 1):
            new_ways = [0] * 10
            for digit, knight_neighbors in enumerate(digit_to_knight_neighbors):
                for neighbor in knight_neighbors:
                    new_ways[neighbor] = (new_ways[neighbor] + ways[digit]) % MOD
            ways = new_ways
        return sum(ways) % MOD
