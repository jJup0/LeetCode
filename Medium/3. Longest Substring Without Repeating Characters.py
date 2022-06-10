class Solution:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        # map last occurance of character
        last_seen = {}

        # current start index of duplicate free substring
        start = 0

        # result variable
        res = 0

        for i, c in enumerate(s):
            # if character has already been seen and is part of current substring
            if c in last_seen and last_seen[c] >= start:
                # update res if necessary
                curr_substring_length = i - start
                if (curr_substring_length > res):
                    res = curr_substring_length

                # increment starting index by one to have duplicate free substring
                start = last_seen[c] + 1

            # update last occurance of c
            last_seen[c] = i

        # return maximum between previous longest substring and current
        return max(res, len(s) - start)
