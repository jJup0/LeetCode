"""
You are given a string s.

You can perform the following process on s any number of times:
- Choose an index i in the string such that there is at least one character to
  the left of index i that is equal to s[i], and at least one character to the
  right that is also equal to s[i].
- Delete the closest character to the left of index i that is equal to s[i].
- Delete the closest character to the right of index i that is equal to s[i].

Return the minimum length of the final string s that you can achieve.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of lowercase English letters.
"""

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Even occurances can always be reduced down to 2, odd occurance counts to 1.
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return sum(2 - (count & 1) for count in Counter(s).values())
