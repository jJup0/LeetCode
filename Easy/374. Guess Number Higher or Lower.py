# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# def guess(val: int) -> int:
#     valToGuess = #a number
#     if val == valToGuess:
#         return 0
#     return 1 if val > valToGuess else -1


class Solution:
    """
    We are playing the Guess Game. The game is as follows:

    I pick a number from 1 to n. You have to guess which number I picked.

    Every time you guess wrong, I will tell you whether the number I picked is higher or lower than
    your guess.

    You call a pre-defined API int guess(int num), which returns three possible results:
        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).

    Return the number that I picked.

    Constraints:
        1 <= n <= 2^31 - 1
        1 <= pick <= n
    """

    def guessNumber(self, n: int) -> int:
        """
        Simple binary serach approach
        O(log(n)) / O(1)    time / space complexity
        """
        lo = 0
        hi = n
        res = g = -2
        while res:
            g = (lo + hi) >> 1
            res = guess(g)
            if res == -1:
                hi = g - 1
            else:
                lo = g + 1

        return g
