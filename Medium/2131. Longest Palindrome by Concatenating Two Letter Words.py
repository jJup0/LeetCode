from collections import Counter
from typing import List


class Solution:
    """
    You are given an array of strings words. Each element of words consists of two lowercase
    English letters.

    Create the longest possible palindrome by selecting some elements from words and concatenating
    them in any order. Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. If it is impossible to create
    any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.

    Constraints:
        1 <= words.length <= 10^5
        words[i].length == 2
        words[i] consists of lowercase English letters.
    """

    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)

        # if a valid center has been found, i.e. a word with two of the same letters
        center = False

        # result variable
        res = 0
        for word, count in counter.items():
            a, b = word
            if a == b:
                # if word is palindrome, and count is odd, then a center has been found, else use
                # all occurances to build palindrome from both sides
                if count & 1:
                    center = True
                # use rest of the count to build palindrome
                res += 4 * (count // 2)
            else:
                rev = b + a
                # use if-check to avoid dict size change
                if rev in counter:
                    # get minimum count of current word and its reverse, and use minimum count
                    # (all availible) to build palindrome
                    min_count = min(count, counter[rev])
                    res += 4 * min_count
                    counter[rev] -= min_count
                    counter[word] -= min_count

        # add length 2 to res if center was found
        return res + (center * 2)
