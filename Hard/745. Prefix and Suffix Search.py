from typing import List


class WordFilter_Set_NotWorkingYet:
    """
    Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.
    Implement the WordFilter class:
    WordFilter(string[] words) Initializes the object with the words in the dictionary.
    f(string prefix, string suffix) Returns the index of the word in the dictionary, which has
    the prefix prefix and the suffix suffix. If there is more than one valid index, return the
    largest of them. If there is no such word in the dictionary, return -1.
    Constraints:
        1 <= words.length <= 15000
        1 <= words[i].length <= 10
        1 <= prefix.length, suffix.length <= 10
        words[i], prefix and suffix consist of lower-case English letters only.
        At most 15000 calls will be made to the function f.
    """

    def __init__(self, words: List[str]):
        # create prefix and suffix Trie,
        # each 'node' contains bitmap of which words have that prefix, and mapping to further sub-tries
        self.prefix_trie = {}
        self.suffix_trie = {}

        # add all words to both tries
        for i, word in enumerate(words):
            # bit map representation of word
            curr = self.prefix_trie
            for c in word:
                if c not in curr:
                    curr[c] = ([], set(), {})
                curr[c][0].append(i)
                curr[c][1].add(i)
                curr = curr[c][2]

            curr = self.suffix_trie
            for c in reversed(word):
                if c not in curr:
                    curr[c] = ([], set(), {})
                curr[c][0].append(i)
                curr[c][1].add(i)
                curr = curr[c][2]

    def f(self, prefix: str, suffix: str) -> int:
        # get bit map of which words have given prefix
        prefix_trie = self.prefix_trie
        prefix_list = []
        prefix_set = set()
        for c in prefix:
            if c in prefix_trie:
                prefix_list, prefix_set, prefix_trie = prefix_trie[c]
            else:
                # if prefix does not exist, bit map = 0x0
                pre_val = []
                prefix_set = set()
                break

        # get bit map of which words have given prefix
        suffix_trie = self.suffix_trie
        suffix_list = []
        suffix_set = set()
        for c in suffix:
            if c in suffix_trie:
                suffix_list, suffix_set, suffix_trie = suffix_trie[c]
            else:
                # if prefix does not exist, bit map = 0x0
                suffix_list = []
                suffix_set = set()
                break

        # perform logical and on bitmaps,
        # and get highest set bit = index of word with given prefix and suffix
        if (len(suffix_list) < len(prefix_list)):
            for word_idx in reversed(suffix_list):
                if word_idx in prefix_set:
                    return word_idx
        else:
            for word_idx in reversed(prefix_list):
                if word_idx in suffix_set:
                    return word_idx
        return -1


class WordFilterBitMap:
    """
    Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.
    Implement the WordFilter class:
    WordFilter(string[] words) Initializes the object with the words in the dictionary.
    f(string prefix, string suffix) Returns the index of the word in the dictionary, which has
    the prefix prefix and the suffix suffix. If there is more than one valid index, return the
    largest of them. If there is no such word in the dictionary, return -1.
    Constraints:
        1 <= words.length <= 15000
        1 <= words[i].length <= 10
        1 <= prefix.length, suffix.length <= 10
        words[i], prefix and suffix consist of lower-case English letters only.
        At most 15000 calls will be made to the function f.
    """

    def __init__(self, words: List[str]):
        # create prefix and suffix Trie,
        # each 'node' contains bitmap of which words have that prefix, and mapping to further sub-tries
        self.pre = {}
        self.suff = {}

        # add all words to both tries
        for i, word in enumerate(words):
            # bit map representation of word
            bitmap_val = 1 << i
            curr = self.pre
            for c in word:
                if c not in curr:
                    curr[c] = [0, {}]
                curr[c][0] |= bitmap_val
                curr = curr[c][1]

            curr = self.suff
            for c in reversed(word):
                if c not in curr:
                    curr[c] = [0, {}]
                curr[c][0] |= bitmap_val
                curr = curr[c][1]

    def f(self, prefix: str, suffix: str) -> int:
        # get bit map of which words have given prefix
        pre = self.pre
        pre_val = 0
        for c in prefix:
            if c in pre:
                pre_val, pre = pre[c]
            else:
                # if prefix does not exist, bit map = 0x0
                pre_val = 0
                break

        # get bit map of which words have given suffix
        suff = self.suff
        suff_val = 0
        for c in reversed(suffix):
            if c in suff:
                suff_val, suff = suff[c]
            else:
                # if suffix does not exist, bit map = 0x0
                suff_val = 0
                break

        # perform logical and on bitmaps,
        # and get highest set bit = index of word with given prefix and suffix
        words_bit = pre_val & suff_val

        # if words_bit == 0, this will return -1 as specified
        return words_bit.bit_length()-1


# S = WordFilter(["apple"])
# print(S.f("a", "e"))

S = WordFilter(["cabaabaaaa", "ccbcababac"])
print(S.f("bccbacbcba", "a"))
# ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
# [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],
# ["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
