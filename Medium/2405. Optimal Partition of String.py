class Solution:
    """
    Given a string s, partition the string into one or more substrings such that the
    characters in each substring are unique. That is, no letter appears in a single
    substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a partition.

    Constraints:
        1 <= s.length <= 10^5
        s consists of only English lowercase letters.
    """

    def partitionString(self, s: str) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # characters in the current partition
        char_set = set()
        res = 0
        for c in s:
            # every time a character is reached that is already
            # in the partition, create a new partition
            if c in char_set:
                res += 1
                char_set.clear()
            char_set.add(c)

        # add current partition to total sum of partitions
        return res + 1
