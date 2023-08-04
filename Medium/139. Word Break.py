class Solution:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can
    be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.
    """

    def wordBreak(self, s: str, word_list: list[str]) -> bool:
        """
        Dynamic programming approach.
        O(n^2 + m) / O(n + sizeof(word_dict))   time / space complexity
        """
        # maximum length of any word in word dict
        word_lens = sorted(len(word) for word in word_list)

        # make words into set for O(1) lookup
        word_set: frozenset[str] = frozenset(word_list)

        n = len(s)

        # whether or not s[:i] is known to be able to be constructed
        idx_constructable = [True] + [False] * n
        # bfs front for indexes i such that s[:i] can be build from words in word list
        start_idxs = set([0])
        # while there are s[:i] that can be built, try to find words
        # to append to s[:i] to make some s[:j]
        while start_idxs:
            # take any starting index
            start_idx = start_idxs.pop()
            # iterate through all word lengths and check if the substring s[i:i+word_len] exists in word_set
            for word_len in word_lens:
                stop_idx = word_len + start_idx
                # no need to check further lengths if stop_idx is out of bounds
                if stop_idx > n:
                    break
                # no need to check if already known that s[i:i+word_len] can be built
                if idx_constructable[stop_idx]:
                    continue
                substr = s[start_idx:stop_idx]
                # check if the substring exists in word_set
                if substr in word_set:
                    if n == stop_idx:
                        # if the full word can be constructed, return True
                        return True
                    start_idxs.add(stop_idx)
                    idx_constructable[stop_idx] = True

        # the word cannot be constructed, return False
        return False
