"""
Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word. Return all
such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Constraints:
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.
- Input is generated in a way that the length of the answer doesn't exceed 10^5.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """
        n := len(s), m := len(wordDict)
        O(m^n) / O(m^n)   time / space complexity
        """
        # for each index i in s find words that are equal to s[i:i+len(word)]
        self.compatible_words_starting: list[list[str]] = [[] for _ in range(len(s))]
        for word in wordDict:
            idx_in_s = s.find(word)
            while idx_in_s != -1:
                self.compatible_words_starting[idx_in_s].append(word)
                idx_in_s = s.find(word, idx_in_s + 1)

        # initialize instance variables for helper function
        self.s = s
        self.wordDict = wordDict
        self.sentences: list[str] = []
        self.current_words_in_sentence: list[str] = []

        self._word_break_recursive(0)
        return self.sentences

    def _word_break_recursive(self, s_i: int):
        if s_i >= len(self.s):
            self.sentences.append(" ".join(self.current_words_in_sentence))
            return

        for compatible_word in self.compatible_words_starting[s_i]:
            self.current_words_in_sentence.append(compatible_word)
            self._word_break_recursive(s_i + len(compatible_word))
            self.current_words_in_sentence.pop()
