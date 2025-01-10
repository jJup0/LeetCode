"""
You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1
and str2:
- isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a
  suffix of str2, and false otherwise.

For example, isPrefixAndSuffix("aba","ababa") is true because"aba" is a prefix
of"ababa" and also a suffix, but isPrefixAndSuffix("abc","abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j,
and isPrefixAndSuffix(words[i], words[j]) is true.

Constraints:
- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 10^5
- words[i] consists only of lowercase English letters.
- The sum of the lengths of all words[i] does not exceed 5 * 10^5.
"""

from collections import defaultdict
from typing import Any


class Solution:
    """
    Complexity definitions:
    n := len(words)
    m := average length of words
    """

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        return self.countPrefixSuffixPairs_trie(words)

    def countPrefixSuffixPairs_brute(self, words: list[str]) -> int:
        """
        High complexity, fails tests but works for "Count Prefix and Suffix Pairs I".
        Complexity:
            Time: O(n^2 * m)
            Space: O(1)
        """
        res = 0
        for j, word2 in enumerate(words):
            for i in range(j):
                word1 = words[i]
                res += word2.startswith(word1) and word2.endswith(word1)
        return res

    def countPrefixSuffixPairs_trie(self, words: list[str]) -> int:
        """
        Complextiy:
            Time: O(n * m)
            Space: O(n * m)
        """

        def recursive_default_dict() -> defaultdict[Any, Any]:
            return defaultdict(recursive_default_dict)

        # key in the trie which holds the amount of previous words.
        # can be set to anything that is not a string of length 2
        # consisting of lowercase letters (to avoid collision with
        # actual trie entries)
        COUNT_KEY = "$"
        # trie
        trie_root = recursive_default_dict()
        res = 0
        for w in words:
            curr_trie = trie_root
            for prefix_char, suffix_char in zip(w, reversed(w)):
                curr_trie = curr_trie[prefix_char + suffix_char]
                # previous word is prefix and suffix of current word
                res += curr_trie.get(COUNT_KEY, 0)
            curr_trie[COUNT_KEY] = curr_trie.get(COUNT_KEY, 0) + 1
        return res

    def countPrefixSuffixPairs_lc_optimized(self, words: list[str]) -> int:
        """
        Time complexity as bad as brute force, but works well with the
        test cases provided by leetcode.
        Complextiy:
            Time: O(n^2 * m)
            Space: O(n * m)
        """
        # mapping from previous string to occurance count
        counts: dict[str, int] = {}
        res = 0
        for word in words:
            for prev_word, count in counts.items():
                if word.startswith(prev_word) and word.endswith(prev_word):
                    res += count
            counts[word] = counts.get(word, 0) + 1
        return res


def test():
    s = Solution()
    res = s.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"])
    assert res == 2, res


def speed_test():
    """
    Used to show that implementation which is fast on leetcode is extremely
    slow for random test cases where len(words) is high, but still within
    constraints, including The sum of the lengths of all words[i] does not exceed 5 * 10^5.
    """
    import random
    import timeit

    s = Solution()

    def t_trie():
        s.countPrefixSuffixPairs_trie(words)

    def t_lc():
        s.countPrefixSuffixPairs_lc_optimized(words)

    def t_brute():
        s.countPrefixSuffixPairs_brute(words)

    # speed test to show that trie is much better for large random instances
    repeat_nr = 1
    n_scale = 80_000
    m_scale = 5
    for n in range(n_scale, 5 * n_scale, n_scale):
        for m in range(m_scale, 10 * m_scale, 2 * m_scale):
            words = [
                "".join(chr(random.randint(ord("a"), ord("z"))) for _ in range(m))
                for _ in range(n)
            ]
            total_chars = sum(map(len, words))
            print(f"{n=} {m=} {total_chars=:_}")
            print(f"trie            {timeit.timeit(t_trie, number=repeat_nr):.2f}")
            print(f"small optimized {timeit.timeit(t_lc, number=repeat_nr):.2f}")
            print(f"brute           {timeit.timeit(t_brute, number=repeat_nr):.2f}")
            print(f"---------------")
