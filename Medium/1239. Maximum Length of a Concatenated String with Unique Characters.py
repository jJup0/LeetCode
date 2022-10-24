import functools
from typing import List


class Solution:
    """
    You are given an array of strings arr. A string s is formed by the concatenation of a
    subsequence of arr that has unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by deleting some or no
    elements without changing the order of the remaining elements.

    Constraints:
        1 <= arr.length <= 16
        1 <= arr[i].length <= 26
        arr[i] contains only lowercase English letters.
    """

    def maxLength(self, arr: List[str]) -> int:
        """
        c := number of unique characters, in this case maximum of 26
        O(2^c + n) / O(n)     time / space complexity
        """
        # lengths and bitmaps of strings in arr
        bitmaps = []
        lenghts = []

        # get bitmaps of all strings that contain only unique characters
        # usually would do length check as well, but this is guaranteed in the constraints
        ord_a = ord('a')
        for s in arr:
            if len(set(s)) == len(s):
                bitmaps.append(functools.reduce(lambda x, y: x | (1 << (ord(y) - ord_a)), s, 0))
                lenghts.append(len(s))

        # calculates self.maxLength(arr)
        # i is current index in bitmaps, prev_bm is the bitmap of
        # the concatenated string so far, and used is how many letters have been used so far
        def _maxLength(i: int, prev_bm: int, used: int) -> int:
            if i == len(bitmaps):
                return used

            keep_bm = 0
            # if string represented by bitmaps[i] does not contain any letters present in prev_bm
            # continue recursion by adding bitmap[i]
            if not (prev_bm & bitmaps[i]):
                keep_bm = _maxLength(i + 1, prev_bm | bitmaps[i], used + lenghts[i])

            # return maximum result between using and not using string represented by bitmaps[i]
            return max(keep_bm, _maxLength(i + 1, prev_bm, used))

        return _maxLength(0, 0, 0)

    def maxLength_simple_stolen(self, arr: List[str]) -> int:
        """
        c := number of unique characters, in this case maximum 26
        O(2^c * n) / O(2^c)     time / space complexity
        """

        dp = [set()]
        for s in arr:
            set_s = set(s)
            if len(set_s) == len(s):
                dp.extend(prev | set_s
                          for prev in dp.copy()
                          if (not (prev & set_s)))

        return max(len(set_s) for set_s in dp)
