from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = len(secret) - sum((Counter(secret)-Counter(guess)).values())
        bulls = 0
        for sc, gc in zip(secret, guess):
            bulls += (sc == gc)
        return f"{bulls}A{cows-bulls}B"
