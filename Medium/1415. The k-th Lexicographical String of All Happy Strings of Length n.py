"""
A happy string is a string that:
- consists only of letters of the set ['a','b','c'].
- s[i]!= s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings"abc","ac","b" and"abcbabcbcb" are all happy strings and
strings"aa","baa" and"ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n
sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less
than k happy strings of length n.

Constraints:
- 1 <= n <= 10
- 1 <= k <= 100
"""

from typing import Generator


class Solution1:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Naive, generate the first k happy strings. Passes leetcode tests.
        Complexity:
            Time: O(k) == O(2**n)
            Space: O(n)
        """
        generator = self.happy_string_generator(n, [])
        for _ in range(k - 1):
            if next(generator, None) is None:
                return ""
        return "".join(next(generator, [""]))

    def happy_string_generator(
        self, n: int, prev_chars: list[str]
    ) -> Generator[list[str], None, None]:
        if len(prev_chars) == n:
            yield prev_chars
            return

        chars = "abc"
        prev_char = prev_chars[-1] if prev_chars else ""

        for char in chars:
            if char == prev_char:
                continue
            prev_chars.append(char)
            yield from self.happy_string_generator(n, prev_chars)
            prev_chars.pop()


class Solution2:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Exploit the fact that we know the amount of happy strings of
        length n to directly find the kth happy string.
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # for an alphabet of length x there are `x * (x-1) ** (n-1)` happy
        # strings of length n because after choosing the first letter for
        # each subsequent letter we can only choose from (x-1) characters
        total_happy = 3 * 2 ** (n - 1)
        if k > total_happy:
            return ""

        # make k 0-indexed
        k -= 1
        remaining_happy_possibilities = total_happy // 3
        # result string builder, initialize with empty string so we can check "last character"
        result_chars: list[str] = [""]
        for _ in range(n):
            # no equal consecutive characters allowed
            allowed_chars = "abc".replace(result_chars[-1], "")

            # based on how much of k we have left, choose either the
            # first or second (or in first iteration third) character,
            # use modulo result for k of next iteration
            char_idx, k = divmod(k, remaining_happy_possibilities)

            result_chars.append(allowed_chars[char_idx])
            remaining_happy_possibilities //= 2

        return "".join(result_chars)


class Solution(Solution2):
    pass


def simple_test():
    s = Solution2()
    res = s.getHappyString(1, 3)
    real = "c"
    assert res == real, res

    res = s.getHappyString(3, 9)
    real = "cab"
    assert res == real, res

    res = s.getHappyString(10, 50)
    real = "ababcbabac"
    assert res == real, f"\n{real}\n{res}"


def performance_test():
    import random
    import sys
    import time

    sys.setrecursionlimit(10000)

    s1 = Solution1()
    s2 = Solution2()

    n_magnitude = 6
    for n in range(n_magnitude, n_magnitude * 4, n_magnitude):
        k_magnitude = 2 ** (n - 2)
        for k in range(
            1, k_magnitude, k_magnitude // 4 + random.randint(1, k_magnitude // 10 + 1)
        ):
            t1 = time.perf_counter_ns()
            res1 = s1.getHappyString(n, k)
            t2 = time.perf_counter_ns()
            res2 = s2.getHappyString(n, k)
            t3 = time.perf_counter_ns()
            print(f"{n=}, {k=}")
            print(f"Solution 1: {(t2-t1)//1_000_000}ms")
            print(f"Solution 2: {(t3-t2)//1_000_000}ms")
            print(f"-" * 32)
            print(res2)
            assert res1 == res2


simple_test()
performance_test()
