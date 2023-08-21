class Solution:
    """
    Given a string s, check if it can be constructed by taking a substring of
    it and appending multiple copies of the substring together.

    Constraints:
    - 1 <= s.length <= 10^4
    - s consists of lowercase English letters.
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        return self._repeated_substring_pattern_string_trick(s)

    def _repeated_substring_pattern_string_trick(self, s: str) -> bool:
        """
        If the s is formed by a repeated substring x, then s == x + x + ... x,
        i.e. s == k * x, whereby k >= 2.

        If we concatenate s to itself, we get s + s = (2 * k) * x.

        If we then remove the first and last letter of (s + s),
        we get: (s + s)[1:-1] == y + ((2 * k - 2) * x) + z.

        Since k >= 2, we know (2 * k - 2) >= k.

        Therefore s == k * x is contained within (2 * k - 2) * x.
        So s is a substring of (s + s)[1:-1] and we return True.


        Now for the other case: s is not formed by a repeated substring.
        There exists no k >= 2  that s == k * x.
        Then there is no way to factor (s + s)[1:-1].
        And so s will not be a substring of (s + s)[1:-1], and we return False.

        O(n) / O(n)     time / space complexity
        """
        s_double = s[1:] + s[:-1]
        return s in s_double

    def _repeated_substring_pattern(self, s: str) -> bool:
        """
        Test all factors x of the length of s for if s can be constructed by
        repeating the first x characters.
        Can be improved with prime number sieving.
        O(n^2) / O(1)     time / space complexity
        """
        length = len(s)
        for substr_len in range(length // 2, 0, -1):
            if length % substr_len != 0:
                continue

            # check if s[substr_len:] can be repeated to form s
            is_repeated = True
            for i in range(substr_len, length):
                if s[i] != s[i % substr_len]:
                    is_repeated = False
                    break
            if is_repeated:
                return True

        return False
