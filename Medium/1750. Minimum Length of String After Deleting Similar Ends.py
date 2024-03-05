"""
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked
to apply the following algorithm on the string any number of times:

Return the minimum length of s after performing the above operation any number
of times (possibly zero times).

1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
3. The prefix and the suffix should not intersect at any index.
4. The characters from the prefix and suffix must be the same.
5. Delete both the prefix and the suffix.

Constraints:
- 1 <= s.length <= 10^5
- s only consists of characters 'a', 'b', and 'c'.
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Greedily cut as many characters from start and end of string as possible.
        O(n) / O(1)     time / space complexity
        """
        i = 0
        j = len(s) - 1
        # cut off prefixes and suffixes as long as there are two characters left
        while i < j:
            l = s[i]
            r = s[j]
            if l != r:
                # unequal first and last character, cannot remove any more characters
                break
            while i <= j and s[i] == l:
                i += 1
            while j >= i and s[j] == r:
                j -= 1

        # return length of substring which can no longer be cut down
        return j - i + 1
