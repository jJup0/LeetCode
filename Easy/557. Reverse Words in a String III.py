class Solution:
    """
    Given a string s, reverse the order of characters in each word within a
    sentence while still preserving whitespace and initial word order.

    Constraints:
    - 1 <= s.length <= 5 * 10^4
    - s contains printable ASCII characters.
    - s does not contain any leading or trailing spaces.
    - There is at least one word in s.
    - All the words in s are separated by a single space.
    """

    def reverseWords(self, s: str) -> str:
        """
        O(n) / O(n)     time / space complexity
        """
        # split, reverse and rejoin
        return " ".join(word[::-1] for word in s.split())
