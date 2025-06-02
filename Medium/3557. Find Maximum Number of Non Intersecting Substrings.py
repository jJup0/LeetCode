"""
You are given a string word.

Return the maximum number of non-intersecting substrings of word that are at
least four characters long and start and end with the same letter.

Constraints:
- 1 <= word.length <= 2 * 10^5
- word consists only of lowercase English letters.
"""

import string


class Solution1:
    def maxSubstrings(self, word: str) -> int:
        """
        Memoize maxSubstrings(word[:i]) and keep track of previous occurances of characters.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # previous indexes of characters in word
        prev_occs: dict[str, list[int]] = {c: [] for c in string.ascii_lowercase}
        # dp[i] = maxSubstrings(word[:i])
        dp = [0] * (len(word) + 1)
        for i, c in enumerate(word, start=1):
            dp[i] = dp[i - 1]
            # check previous occurances of character in reverse order
            for prev_occ in reversed(prev_occs[c]):
                if i - prev_occ >= 3:
                    # If previous occurance is at least 3 characters away, we can
                    # make a string with length of at least 4, update dp[i] if
                    # maximum subtrings before this word + 1 is best so far. Can
                    # break afterwards as increasing current word length will not
                    # lead to better results.
                    dp[i] = max(dp[i], dp[prev_occ - 1] + 1)
                    break
            prev_occs[c].append(i)
        return dp[-1]


class Solution2:
    def maxSubstrings(self, word: str) -> int:
        """
        Track characters since last substring, three indexes behind current index.
        Simplicity leads to much faster performance.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        # set of characters 3 before current
        curr_chars: set[str] = set()
        # current pointer in word
        r = 3
        res = 0
        while r < len(word):
            curr_chars.add(word[r - 3])
            if word[r] in curr_chars:
                res += 1
                curr_chars = set()
                r += 4
            else:
                r += 1

        return res


class Solution(Solution2):
    pass


def performance_test():
    import random
    import string
    import timeit

    word = "".join(random.choices(string.ascii_lowercase, k=10000))
    s1 = Solution1()
    s2 = Solution2()

    # Time Solution 1
    t1 = timeit.timeit(lambda: s1.maxSubstrings(word), number=100)

    # Time Solution 2
    t2 = timeit.timeit(lambda: s2.maxSubstrings(word), number=100)

    print(f"Solution 1 time: {t1:.4f}s")
    print(f"Solution 2 time: {t2:.4f}s")


def test():
    s = Solution()
    res = s.maxSubstrings("bcdaaaab")
    real = 1
    assert res == real, res


test()
performance_test()
