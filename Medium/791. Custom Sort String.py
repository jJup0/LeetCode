"""
You are given two strings order and s. All the characters of order are unique
and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order, then
x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Constraints:
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All the characters of order are unique.
"""

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = Counter(s)
        res_char_arr: list[str] = []
        for c in order:
            count = char_count.pop(c, 0)
            if not count:
                continue
            res_char_arr.append(c * count)

        for c, count in char_count.items():
            res_char_arr.append(c * count)

        return "".join(res_char_arr)


s = Solution()
res = s.customSortString("cba", "abcd")
assert res == "cbad"
