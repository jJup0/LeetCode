"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these
characters a, b and c.

Constraints:
- 3 <= s.length <= 5 x 10^4
- s only consists of a, b or c characters.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        a = b = c = 0
        j = 0
        res = 0
        for i, char in enumerate(s):
            if char == "a":
                a += 1
            elif char == "b":
                b += 1
            else:
                c += 1

            while a * b * c > 0:
                res += len(s) - i
                char2 = s[j]
                if char2 == "a":
                    a -= 1
                elif char2 == "b":
                    b -= 1
                else:
                    c -= 1
                j += 1
        return res
