"""
You start with an initial power of power, an initial score of 0, and a bag of
tokens given as an integer array tokens, where each tokens[i] donates the value
of token_i.

Your goal is to maximize the total score by strategically playing these tokens.
In one move, you can play an unplayed token in one of the two ways (but not
both for the same token):
- Face-up: If your current power is at least tokens[i], you may play token_i,
  losing tokens[i] power and gaining 1 score.
- Face-down: If your current score is at least 1, you may play token_i, gaining
  tokens[i] power and losing 1 score.

Return the maximum possible score you can achieve after playing any number of
tokens.

Constraints:
- 0 <= tokens.length <= 1000
- 0 <= tokens[i], power < 10^4
"""


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        """
        Greedily play lowest valued tokens face up to gain score,
        and high value tokens face down to gain power.
        O(n * log(n)) / O(1)    time / space complexity
        """
        # sort tokens by value to optimally, greedily play face up or down
        tokens.sort()

        # i is index of next token to play face up
        i = 0
        # j is next index of token to play face down
        j = len(tokens) - 1

        score = 0
        # while there are unused tokens
        while i <= j:
            # play lowest value unplayed token face up while power is sufficient
            for i in range(i, j + 1):
                if power < tokens[i]:
                    break
                power -= tokens[i]
                score += 1

            if score == 0 or i >= j:
                # if score is 0 then no score can be sacrificed
                # if i >= j then there are less than two tokens remaining,
                # and it is not possible/sensible to play a token face down
                break

            # play the largest uplayed token face down
            power += tokens[j]
            j -= 1
            score -= 1

        return score
