"""
You are given a string word and an integer k.

We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for
all indices i and j in the string.

Here, freq(x) denotes the frequency of the character x in word, and |y| denotes
the absolute value of y.

Return the minimum number of characters you need to delete to make word k-special.

Constraints:
- 1 <= word.length <= 10^5
- 0 <= k <= 10^5
- word consists only of lowercase English letters.
"""

import itertools
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        return self.minimumDeletions2(word, k)

    def minimumDeletions2(self, word: str, k: int) -> int:
        counts = sorted(Counter(word).values())
        accu_counts = list(itertools.accumulate(counts))
        curr_to_delete = 0
        res = len(word)
        j = 0
        for i in range(len(counts)):
            # remove all counts in `counts[:i]`
            curr_min_count = counts[i]
            curr_res = curr_to_delete
            for j in range(j, len(counts)):
                if counts[j] - curr_min_count > k:
                    j -= 1
                    break

            # counts[i:j+1] stay as they are
            pass

            # reduce counts[j+1:] to curr_min_count
            sum_rest = accu_counts[-1] - accu_counts[j]
            nr_of_rest = len(counts) - j - 1
            reduction = sum_rest - (curr_min_count + k) * nr_of_rest
            curr_res += reduction

            res = min(res, curr_res)
            curr_to_delete += curr_min_count

        return res

    def minimumDeletions1(self, word: str, k: int) -> int:
        """
        Complexity:
            x:= size of alphabet
            Time: O(n + x^2)
            Space: O(x)
        """
        counts = sorted(Counter(word).values())
        res = len(word)
        for smallest in counts:
            curr_res = 0
            for count in counts:
                if count < smallest:
                    curr_res += count
                delta = count - k - smallest
                if delta > 0:
                    curr_res += delta
            if curr_res < res:
                res = curr_res
        return res


def test():
    sol = Solution()
    res = sol.minimumDeletions("aabcaba", 0)
    assert res == 3, res


def big_alphabet_test():
    import random
    import timeit

    sol = Solution()

    alphabet_size = 5000
    word_size = 10000
    word = "".join(chr(random.randint(1, alphabet_size)) for _ in range(word_size))
    k = random.randint(1, 1000)

    real = sol.minimumDeletions1(word, k)
    res = sol.minimumDeletions2(word, k)
    assert real == res
    print("v2 is correct")

    print(f"v1=", timeit.timeit(lambda: sol.minimumDeletions1(word, k), number=1))
    print(f"v2=", timeit.timeit(lambda: sol.minimumDeletions2(word, k), number=1))


test()
big_alphabet_test()
