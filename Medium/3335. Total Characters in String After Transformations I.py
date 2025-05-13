"""
You are given a string s and an integer t, representing the number of
transformations to perform. In one transformation, every character in s is
replaced according to the following rules:
- If the character is'z', replace it with the string"ab".
- Otherwise, replace it with the next character in the alphabet. For
  example,'a' is replaced with'b','b' is replaced with'c', and so on.

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters.
- 1 <= t <= 10^5
"""

from functools import cache


class Solution:
    MOD = 10**9 + 7

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        return sum(self.char_length_after_t(c, t) for c in s) % self.MOD

    @classmethod
    @cache
    def char_length_after_t(cls, c: str, t: int) -> int:
        steps_to_ab = ord("z") - ord(c) + 1
        if t < steps_to_ab:
            return 1
        t -= steps_to_ab
        return (
            cls.char_length_after_t("a", t) + cls.char_length_after_t("b", t)
        ) % cls.MOD


def test():
    import random
    import string

    sol = Solution()
    s = "".join(random.choice(string.ascii_lowercase))
    res = sol.lengthAfterTransformations(s, 10000)
    print(res)


test()
