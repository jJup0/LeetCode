class Solution:
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in
    haystack, or -1 if needle is not part of haystack.

    Constraints:
        1 <= haystack.length, needle.length <= 10^4
        haystack and needle consist of only lowercase English characters.
    """

    def strStr(self, haystack: str, needle: str) -> int:
        """
        O(n * m) / O(m)     time / space complexity
        """
        # built-in variation: return haystack.find(needle)

        # iterate through all positions in haystack, where the character at that position is the
        # same as the first character in needle
        starting_indexes = (i for i, c in enumerate(haystack) if c == needle[0])
        for haystack_index in starting_indexes:
            # simple subtring equality comparison
            if haystack[haystack_index:haystack_index + len(needle)] == needle:
                return haystack_index

        # return -1 if not found
        return -1
