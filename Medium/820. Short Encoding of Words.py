from typing import List


class Solution:
    """
    A valid encoding of an array of words is any reference string s and array of indices indices such that:
        words.length == indices.length
        The reference string s ends with the '#' character.
        For each index indices[i], the substring of s starting from indices[i] and up to (but not including)
        the next '#' character is equal to words[i].
    Given an array of words, return the length of the shortest reference string s possible of any valid
    encoding of words.
    Constraints:
        1 <= words.length <= 2000
        1 <= words[i].length <= 7
        words[i] consists of only lowercase letters.
    """

    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        n:= len(words), c:=sum(len(word) for word in words)
        O(n*log(n) + c) time, O(c) space
        """
        # encoding for words can only be shorter if words share suffixes

        # result variable
        res = 0

        # sort words by length descending
        words.sort(key=lambda x: len(x), reverse=True)

        # create a trie for words in reverse order
        suffix_trie = {}

        for word in words:
            curr = suffix_trie
            is_suffix = True
            # add word in revers to trie
            for c in reversed(word):
                if c not in curr:
                    # if any letter is not already in trie, then this word is not a suffix of any other word
                    is_suffix = False
                    curr[c] = {}
                curr = curr[c]
            # if it is not a suffix, add its length + 1 to result (+1 for the #)
            if not is_suffix:
                res += len(word) + 1
        return res

    def minimumLengthEncodingAlternative(self, words: List[str]) -> int:
        """
        n:= len(words), c:=sum(len(word) for word in words), l = c/n <= 7 due to constraint
        this alternative algorithm works faster for guaranteed short words
        O(l * n * log(n) + c) time, O(c) space
        """
        # sort words so that suffixes (shorter words) come last
        sorted_words = sorted((word[::-1] for word in words), reverse=True)
        res = 0
        prev = ''
        # go through sorted reversed words, where word could only be suffix of prev
        for word in sorted_words:
            # len(word) <= 7, no need to check word != prev in O(1)
            if not prev.startswith(word):
                res += len(word) + 1
            prev = word
        return res
