"""
Two strings are considered close if you can attain one from the other using the
following operations:
- Operation 1: Swap any two existing characters. 
  - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into
  another existing character, and do the same with the other character. 
  - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close,
and false otherwise.

Constraints:
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.
"""


from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Operation 1 lets us treat strings as bags of characters (with no order).
        Operation 2 lets two strings be similar if the have the same counts regardless
        of character, and the same character set.
        O(n) / O(n)     time / space
        """
        counter_w1 = Counter(word1)
        counter_w2 = Counter(word2)
        # values are treated as ordered collections, so two compare equality of
        # counts, put them in another Counter
        counts_compatible = Counter(counter_w1.values()) == Counter(counter_w2.values())
        char_sets_compatible = counter_w1.keys() == counter_w2.keys()
        return counts_compatible and char_sets_compatible
