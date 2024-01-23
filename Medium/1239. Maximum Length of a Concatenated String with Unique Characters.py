"""
You are given an array of strings arr. A string s is formed by the
concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= arr.length <= 16
- 1 <= arr[i].length <= 26
- arr[i] contains only lowercase English letters.
"""
import functools


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        return self.maxLength_bitmap(arr)

    def maxLength_bitmap(self, arr: list[str]) -> int:
        """
        c := number of unique characters, in this case maximum of 26
        O(2^c + n) / O(n)     time / space complexity
        """
        # lengths and bitmaps of strings in arr
        bitmaps: list[int] = []
        lenghts: list[int] = []

        # get bitmaps of all strings that contain only unique characters
        ord_a = ord("a")
        for s in arr:
            if len(set(s)) != len(s):
                # ignore strings with duplicate letters
                continue
            # create a bitmap representation of the string
            bitmap = functools.reduce(
                lambda bitmap, char: bitmap | (1 << (ord(char) - ord_a)), s, 0
            )
            bitmaps.append(bitmap)
            lenghts.append(len(s))

        def _maxLength(i: int, curr_bitmap: int, chars_length: int) -> int:
            """Calculates self.maxLength(arr)

            Args:
                i (int): Current index in bitmaps.
                curr_bitmap (int): Bitmap of the currently simulated concatenated string
                chars_length (int): Length of current string concatenation

            Returns:
                int: Maximum length of concatenated string with unique characters.
            """
            nonlocal bitmaps, lenghts
            if i == len(bitmaps):
                return chars_length

            max_length_no_include = _maxLength(i + 1, curr_bitmap, chars_length)
            if curr_bitmap & bitmaps[i]:
                # if current string is not compatible with character string
                # so far, return result for not including the current string
                return max_length_no_include

            # if the current string is compatible with the string of characters so far,
            # recurse and return the maximum
            max_score_include = _maxLength(
                i + 1,
                curr_bitmap | bitmaps[i],
                chars_length + lenghts[i],
            )
            return max(max_score_include, max_length_no_include)

        return _maxLength(0, 0, 0)

    def maxLength_str_set_simple(self, arr: list[str]) -> int:
        """
        c := number of unique characters, in this case maximum 26
        O(2^c * n) / O(2^c)     time / space complexity
        """

        all_char_sets: list[set[str]] = [set()]
        for string in arr:
            set_s = set(string)
            if len(set_s) != len(string):
                # string itself does not have unique characters
                continue

            # add current string to all compatible previous combinations
            all_char_sets.extend(
                (prev.union(set_s))  # new combined string
                for prev in all_char_sets.copy()  # all previous strings (but make a copy to avoid extra work)
                if not (prev.intersection(set_s))  # compatible if charsets are disjoint
            )

        # return length of largest charset
        return max(len(set_s) for set_s in all_char_sets)
