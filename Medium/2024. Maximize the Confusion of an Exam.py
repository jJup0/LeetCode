"""Solution for leetcode problem "2024. Maximize the Confusion of an Exam".
Description:

A teacher is writing a test with n true/false questions, with 'T' denoting true
and 'F' denoting false. He wants to confuse the students by maximizing the number
of consecutive questions with the same answer (multiple trues or multiple falses
in a row).

You are given a string answerKey, where answerKey[i] is the original answer to
the ith question. In addition, you are given an integer k, the maximum number
of times you may perform the following operation:
- Change the answer key for any question to 'T' or 'F'
  (i.e., set answerKey[i] to 'T' or 'F').
- Return the maximum number of consecutive 'T's or 'F's in the answer key after
  performing the operation at most k times.

Constraints:
- n == answerKey.length
- 1 <= n <= 5 * 10^4
- answerKey[i] is either 'T' or 'F'
- 1 <= k <= n
"""


from collections import deque


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """Repeat same strategy, one time for "T" one time for "F".
        O(n) / O(k)     time / space complexity
        """
        ts = self._max_consecutive(answerKey, k, "T")
        fs = self._max_consecutive(answerKey, k, "F")
        return max(ts, fs)

    def _max_consecutive(self, answer_key: str, k: int, maximize_letter: str) -> int:
        """Create a sliding window of replaced characters.

        Every time a non-`maximize_letter` character is encountered it is replaced
        with `maximize_letter`. If k replacements have already taken place
        "unreplace" the first still existing replacement.

        O(n) / O(k)     time / space complexity
        """
        replacements: deque[int] = deque()
        first_occurance = 0
        res = 0
        for i, c in enumerate(answer_key):
            if c == maximize_letter:
                continue
            if len(replacements) == k:
                res = max(res, i - first_occurance)
                first_occurance = replacements.popleft() + 1
            replacements.append(i)
        res = max(res, len(answer_key) - first_occurance)
        return res
