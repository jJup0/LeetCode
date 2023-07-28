from functools import cache


class Solution:
    """
    You are given an integer array nums. Two players are playing a game with this array:
    player 1 and player 2.

    Player 1 and player 2 take turns, with player 1 starting first. Both players start
    the game with a score of 0. At each turn, the player takes one of the numbers from
    either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the
    size of the array by 1. The player adds the chosen number to their score. The game
    ends when there are no more elements in the array.

    Return true if Player 1 can win the game. If the scores of both players are equal,
    then player 1 is still the winner, and you should also return true. You may assume
    that both players are playing optimally.

    Constraints:
    - 1 <= nums.length <= 20
    - 0 <= nums[i] <= 10^7
    """

    def PredictTheWinner(self, nums: list[int]) -> bool:
        """
        Dynamic programming approach.
        O(n^2) / O(n^2)     time / space complexity
        """
        prefix_sum: list[int] = [0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)

        @cache
        def max_winnings(start: int, stop: int) -> int:
            """Returns maximum winnings for current player for nums[start:stop+1]."""

            # if only one number left to take
            if start == stop:
                return nums[start]

            # after taking the left number, this is the sum of what remains
            # increment
            nums_sum_remaining_l = prefix_sum[stop + 1] - prefix_sum[start + 1]
            # max winning after taking left number is:
            # value of left number + whatever remains after the other player play optimally
            take_left = nums[start] + (
                nums_sum_remaining_l - max_winnings(start + 1, stop)
            )

            # analogously for taking right number
            nums_sum_remaining_r = prefix_sum[stop] - prefix_sum[start]
            take_right = nums[stop] + (
                nums_sum_remaining_r - max_winnings(start, stop - 1)
            )

            # return maximum of left and right strategies
            return max(take_left, take_right)

        # return true iff the maximum winnings are more than or equal to half of sum of numbers
        return max_winnings(0, len(nums) - 1) >= (prefix_sum[-1] / 2)
