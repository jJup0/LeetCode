class Solution:
    """
    You are given an array of words where each word consists of lowercase
    English letters.

    wordA is a predecessor of wordB if and only if we can insert exactly one
    letter anywhere in wordA without changing the order of the other characters
    to make it equal to wordB.

    - For example, "abc" is a predecessor of "abac", while "cba" is not a
      predecessor of "bcad".

    A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
    where word1 is a predecessor of word2, word2 is a predecessor of word3, and
    so on. A single word is trivially a word chain with k == 1.

    Return the length of the longest possible word chain with words chosen from
    the given list of words.

    Constraints:
    - 1 <= words.length <= 1000
    - 1 <= words[i].length <= 16
    - words[i] only consists of lowercase English letters.
    """

    def longestStrChain(self, words: list[str]) -> int:
        """
        O(n * n * word_length) / O(n)   time / space complexity
        """
        # maximum length of a word
        LEN_CONSTRAINT = 16

        # sort words to make iterating easier
        words.sort(key=lambda x: len(x))

        # longest_chain_len[i] = longest chain possible ending with word i
        longest_chain_len = [1] * len(words)

        # words in separate buckets by length
        words_by_len_with_idx: list[list[tuple[int, str]]] = [
            [] for _ in range(LEN_CONSTRAINT + 1)
        ]

        # put words into buckets with their index
        for i, word in enumerate(words):
            words_by_len_with_idx[len(word)].append((i, word))

        for i, word in enumerate(words):
            l = len(word)
            # get all possible predecessors of word
            for j, child_word in words_by_len_with_idx[l - 1]:
                # count character difference
                diff = 0
                for k in range(l):
                    # check how many characters are different, if more than one, break
                    if (k - diff < l - 1) and (child_word[k - diff] != word[k]):
                        diff += 1
                        if diff == 2:
                            break
                else:
                    # if 0 or 1 characters differ, update longest chain for successor word
                    chain_from_predecessor = longest_chain_len[j] + 1
                    if chain_from_predecessor > longest_chain_len[i]:
                        longest_chain_len[i] = chain_from_predecessor

        # return longest chain
        return max(longest_chain_len)
