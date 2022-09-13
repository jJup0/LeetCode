from collections import deque
from typing import List


class Solution:
    """
    You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i]
    is the value of the ith token (0-indexed).
    Your goal is to maximize your total score by potentially playing each token in one of two ways:
        If your current power is at least tokens[i], you may play the ith token face up, losing
        tokens[i] power and gaining 1 score.
        If your current score is at least 1, you may play the ith token face down, gaining tokens[i]
        power and losing 1 score.
    Each token may be played at most once and in any order. You do not have to play all the tokens.
    Return the largest possible score you can achieve after playing any number of tokens.
    Constraints:
        0 <= tokens.length <= 1000
        0 <= tokens[i], power < 10^4
    """

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Use highest valued tokens to play face down, and lowest valued to gain score
        O(n * log(n)) / O(1)    time / space complexity
        """
        tokens.sort()

        # i is index of next token to play face up, j is next index of token to play face down
        i, j = 0, len(tokens) - 1

        score = 0
        # while there are unused tokens
        while i <= j:
            # flip most possible tokens face up
            for i in range(i, j + 1):
                if power < tokens[i]:
                    break
                power -= tokens[i]
                score += 1

            # if there are two or more coins left, flip highest valued unplayed token face down
            if score > 0 and i < j:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break

        return score
