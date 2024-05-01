"""
A wonderful string is a string where at most one letter appears an odd number
of times.
- For example,"ccjjc" and"abab" are wonderful, but"ab" is not.

Given a string word that consists of the first ten lowercase English letters
('a' through'j' ), return the number of wonderful non-empty substrings in word.
If the same substring appears multiple times in word, then count each
occurrence separately.

A substring is a contiguous sequence of characters in a string.

Constraints:
- 1 <= word.length <= 10^5
- word consists of lowercase English letters from 'a' to'j'.
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        m := different amount of characters allowed, in this case 10
        For larger alphabets where 2^m >> n, we could use a dictionary instead.
        O(n * m) / O(2^m)      time / space complexity
        """
        # occurance count of prefix with this character parity
        count = [0] * (1 << 10)
        count[0] = 1
        result = 0
        # current prefix parity
        prefix_parity = 0
        for char in word:
            # update parity
            prefix_parity ^= 1 << (ord(char) - ord("a"))

            # this prefix can be paired with any other prefix with the same
            # parity, as we can just remove those prefixes from this prefix
            # to get a string with all even occurances
            result += count[prefix_parity]

            # this prefix can be paired with any other prefixes with a bit difference of 1
            for i in range(10):
                result += count[prefix_parity ^ (1 << i)]

            # increase occurance count
            count[prefix_parity] += 1

        return result
