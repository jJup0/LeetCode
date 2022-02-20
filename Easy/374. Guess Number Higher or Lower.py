# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guess(val):
    valToGuess = 1
    if val == valToGuess:
        return 0
    return 1 if val > valToGuess else -1


class Solution:
    def guessNumber(self, n: int) -> int:
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
