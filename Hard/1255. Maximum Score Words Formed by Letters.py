"""
Given a list of words, list of single letters (might be repeating) and score of
every character.

Return the maximum score of any valid set of words formed by using the given
letters ( words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only
be used once. Score of letters'a','b','c',...,'z' is given by score[0],
score[1],..., score[25] respectively.

Constraints:
- 1 <= words.length <= 14
- 1 <= words[i].length <= 15
- 1 <= letters.length <= 100
- letters[i].length == 1
- score.length == 26
- 0 <= score[i] <= 10
- words[i], letters[i] contains only lower case English letters.
"""

from collections import Counter


class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        """
        n := len(words), m := sum(len(word) for word in words)
        O(2^n + m) / O(m)       time / space complexity
        """
        self.availible_letters = Counter(letters)
        self.words_as_counter = [Counter(word) for word in words]
        self.score_of_words = [
            sum(score[ord(c) - ord("a")] for c in word) for word in words
        ]
        return self._max_score_words_helper(0, 0)

    def _max_score_words_helper(self, word_i: int, score: int) -> int:
        if word_i == len(self.words_as_counter):
            # return if no more words left
            return score

        # get max result for not using this word
        max_score = self._max_score_words_helper(word_i + 1, score)

        curr_word_as_counter = self.words_as_counter[word_i]
        if curr_word_as_counter < self.availible_letters:
            # if there are enough letters left to use this word, do so
            # remove letters
            self.availible_letters -= curr_word_as_counter
            # go to next word with increased score
            res_if_used = self._max_score_words_helper(
                word_i + 1, score + self.score_of_words[word_i]
            )
            max_score = max(max_score, res_if_used)
            # restore available letters
            self.availible_letters += curr_word_as_counter
        return max_score
