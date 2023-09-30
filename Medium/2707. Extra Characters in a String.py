class Solution:
    """
    You are given a 0-indexed string s and a dictionary of words dictionary.
    You have to break s into one or more non-overlapping substrings such that
    each substring is present in dictionary. There may be some extra characters
    in s which are not present in any of the substrings.

    Return the minimum number of extra characters left over if you break up s optimally.

    Constraints:
    - 1 <= s.length <= 50
    - 1 <= dictionary.length <= 50
    - 1 <= dictionary[i].length <= 50
    - dictionary[i] and s consists of only lowercase English letters
    - dictionary contains distinct words
    """

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        """Dynamic programming approach.
        m = total characters in dictionary
        O(n * m) / O(n * m)     time / space complexity
        """
        n = len(s)
        # mapping from indexes in s to words that s[i:] starts with
        s_i_to_words: dict[int, list[str]] = {i: [] for i in range(n)}
        for word in dictionary:
            prev_occurance_index = 0
            while True:
                idx = s.find(word, prev_occurance_index)
                if idx == -1:
                    break
                s_i_to_words[idx].append(word)
                prev_occurance_index = idx + 1

        # minimum number of left over characters for minExtraChar(s[:i]),
        dp = list(range(n + 1))
        for s_i in range(len(s)):
            # update current dp in case a previous solution is better
            dp[s_i + 1] = min(dp[s_i + 1], dp[s_i] + 1)
            # break s at index s_i and store optimal breaking in dp
            for word in s_i_to_words[s_i]:
                w_len = len(word)
                # using word to break s at s_i:
                # dp[s_i + w_len] has at most dp[s_i] characters left over
                dp[s_i + w_len] = min(dp[s_i + w_len], dp[s_i])

        # return characters left over after optimal breaking
        return dp[-1]
