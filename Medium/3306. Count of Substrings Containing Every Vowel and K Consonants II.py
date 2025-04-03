"""
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel
('a','e','i','o', and'u' ) at least once and exactly k consonants.

Constraints:
- 5 <= word.length <= 2 * 10^5
- word consists only of lowercase English letters.
- 0 <= k <= word.length - 5
"""

from collections import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """Easy to calculate substrings with at least k, so take the difference of at least k and at least k + 1."""
        return self._at_least_k(word, k) - self._at_least_k(word, k + 1)

    def _at_least_k(self, word: str, k: int) -> int:
        """Sliding window approach.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        res = 0
        start = 0
        end = 0
        # keep track of counts of vowels and consonants
        vowel_count: Counter[str] = Counter()
        consonant_count = 0

        # start sliding window
        while end < len(word):
            # insert new letter
            char = word[end]

            # update counts
            if self._is_vowel(char):
                vowel_count[char] += 1
            else:
                consonant_count += 1

            # shrink window while we have a valid substring
            while len(vowel_count) == 5 and consonant_count >= k:
                res += len(word) - end
                start_letter = word[start]
                if self._is_vowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        vowel_count.pop(start_letter)
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return res

    def _is_vowel(self, c: str) -> bool:
        return c in "aeiou"
