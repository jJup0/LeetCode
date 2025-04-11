"""
You are given a string s. You can convert s to a palindrome by adding
characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of lowercase English letters only.
"""


class Solution:
    def shortestPalindrome_naive(self, s: str) -> str:
        """Find longest prefix which is a palindrome.

        Passes leetcode tests (does not time out).

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        for length in range(len(s), 0, -1):
            if s[:length] == s[:length][::-1]:
                return s[length:][::-1] + s
        return ""

    def shortestPalindrome(self, s: str) -> str:
        """Rely on hashing to get longest palindromic prefix.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        mod = 10**9 + 7
        # manual hash of s[:i+1] and s[:i+1][::-1]
        prefix_hash = prefix_reversed_hash = 0
        # hash base, first prime larger than 26
        base = 29
        # Prefix hash can be calculated rolling as normal: multiply previous
        # hash and add hash of current character. This way the first char has
        # been multiplied i times once we get to the ith character.
        # To get the hash of the reverse prefix, we need to multiply the
        # current char by base**i to simulate it being the first character
        # in the hash
        power_for_reverse_prefix = 1

        longest_palin_prefix_len = 0
        for prefix_len, c in enumerate(s, start=1):
            char_hash = ord(c) - ord("a") + 1
            # add to prefix hash as normal
            prefix_hash = (prefix_hash * base + char_hash) % mod
            # add to "back" of reversed prefix hash by not multiplying
            # reversed prefix hash and multiplying char hash by power
            prefix_reversed_hash = (
                prefix_reversed_hash + char_hash * power_for_reverse_prefix
            ) % mod
            # multiply power by base for next char
            power_for_reverse_prefix = (power_for_reverse_prefix * base) % mod

            if prefix_hash == prefix_reversed_hash:
                longest_palin_prefix_len = prefix_len

        # sanity check, as we are only working with hashes
        longest_palindrome_prefix = s[:longest_palin_prefix_len]
        assert longest_palindrome_prefix == longest_palindrome_prefix[::-1], s
        # prepend rest of string after palindrome prefix reversed
        return s[longest_palin_prefix_len:][::-1] + s


def test():
    sol = Solution()
    res = sol.shortestPalindrome("aabba")
    assert res == "abbaabba", res
    res = sol.shortestPalindrome("")
    assert res == "", res


def hash_collision_test():
    import random

    sol = Solution()
    alphabet = list(chr(o) for o in range(ord("A"), ord("z")))
    for i in range(10**4):
        print(f"Round {i}")
        for _ in range(10**6):
            string = "".join(random.choice(alphabet) for _ in range(10))
            sol.shortestPalindrome(string)
