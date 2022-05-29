from typing import List


class Solution:
    """
    Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words
    do not share common letters. If no such two words exist, return 0.
    Constraints:
        2 <= words.length <= 1000
        1 <= words[i].length <= 1000
        words[i] consists only of lowercase English letters.
    """

    def maxProduct(self, words: List[str]) -> int:
        ord_a = ord('a')
        # calculates bit representation of a set of letters of a given word

        def bin_transform(word):
            bin_word = 0
            for c in word:
                bin_word |= 1 << (ord(c) - ord_a)
            return bin_word

        # sort words by length, to allow early break when finding result
        words.sort(key=len, reverse=True)
        # calculate bit representation of each word
        bin_words = [bin_transform(word) for word in words]

        # result variable
        res = 0
        # iterate through all words, in order of length
        for i, bin_word1 in enumerate(bin_words):
            len_i = len(words[i])
            # iterate through all remaining words
            for j, bin_word2 in enumerate(bin_words[i+1:], start=i + 1):
                len_j = len(words[j])
                # if possible score lower than res, break
                if len_i * len_j <= res:
                    break

                # if word[i] and word[j] do not share any bits, update res,
                # product is guaranteed to be bigger than res
                if not (bin_word1 & bin_word2):
                    res = len_i * len_j
        return res
