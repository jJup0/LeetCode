"""
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array
(i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with
arr[1], the larger integer wins and remains at position 0, and the smaller
integer moves to the end of the array. The game ends when an integer wins
k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

Constraints:
- 2 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^6
- arr contains distinct integers.
- 1 <= k <= 10^9
"""


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        """
        No need to simulate placing loser at the back of the queue, only need
        to loop through array once, if no number won k times by the end of the
        game, then the largest number will be the winner of the game.
        O(n) / O(1)     time / space complexity
        """
        win_streak = -1
        winner = arr[0]
        for num in arr:
            if winner >= num:
                win_streak += 1
            else:
                winner = num
                win_streak = 1

            if win_streak == k:
                return winner
        return winner
