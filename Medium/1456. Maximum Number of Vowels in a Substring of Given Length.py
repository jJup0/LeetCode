from collections import deque


class Solution:
    """
    Given a string s and an integer k, return the maximum number of vowel
    letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

    Constraints:
        1 <= s.length <= 10^5
        s consists of lowercase English letters.
        1 <= k <= s.length
    """

    def maxVowels(self, s: str, k: int) -> int:
        """Sliding window method.
        O(n) / O(k)     time / space complexity
        """
        vowels = "aeiou"
        char_deque = deque(s[:k])
        res = curr_vowel_count = sum(c in vowels for c in char_deque)
        for i in range(k, len(s)):
            new_char = s[i]

            # pop last in char from deque
            old_c = char_deque.popleft()
            # if char is a vowel, decreate vowel count
            if old_c in vowels:
                curr_vowel_count -= 1

            # if new char is a vowel, increase vowel count and update res if needed
            if new_char in vowels:
                curr_vowel_count += 1
                if curr_vowel_count > res:
                    res = curr_vowel_count
            # add new char to deque
            char_deque.append(new_char)
        return res
