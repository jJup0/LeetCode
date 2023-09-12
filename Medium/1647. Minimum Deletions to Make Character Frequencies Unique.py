from collections import Counter


class Solution:
    """
    A string s is called good if there are no two different characters in s that
    have the same frequency.

    Given a string s, return the minimum number of characters you need to delete
    to make s good.

    The frequency of a character in a string is the number of times it appears
    in the string. For example, in the string "aab", the frequency of 'a' is 2,
    while the frequency of 'b' is 1.

    Constraints:
    - 1 <= s.length <= 10^5
    - s contains only lowercase English letters.
    """

    def minDeletions(self, s: str) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # mapping from character occurence count to amount of characters
        # that have that count
        char_count_counter = Counter(Counter(s).values())
        result = 0
        # next largest count that is unique
        next_largest_unique = len(s)
        # iterate through counts, sorted by char count decresing
        for char_count, count_count in sorted(char_count_counter.items(), reverse=True):
            # if only one, then it is unique
            if count_count == 1:
                continue

            # update next largest unique to minimum of itself and current char count-1,
            # as we cannot add characters
            next_largest_unique = min(next_largest_unique, char_count - 1)

            # while they count is not unique, and there are unique counts left
            while count_count > 1 and next_largest_unique > 0:
                if next_largest_unique not in char_count_counter:
                    # if the char count that we want to use is unique,
                    # remove characters until it is unique
                    count_count -= 1
                    result += char_count - next_largest_unique

                # in any case, next largest unique count must be decremented
                next_largest_unique -= 1

            # this line accounts for characters which can no longer have
            # a unique count, they must be entirely removed
            result += (count_count - 1) * (char_count - next_largest_unique)

        return result
