"""
You are given a string s and an integer repeatLimit. Construct a new string
repeatLimitedString using the characters of s such that no letter appears more
than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position
where a and b differ, string a has a letter that appears later in the alphabet
than the corresponding letter in b. If the first min(a.length, b.length)
characters do not differ, then the longer string is the lexicographically
larger one.

Constraints:
- 1 <= repeatLimit <= s.length <= 10^5
- s consists of lowercase English letters.
"""

from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """
        Greedily append `repeatLimit` of largest char remaining, if more
        remaining "break" the streak with a single occurance of the
        second largest remaining character.

        m := unique chars in `s`, in this case at most 26, could be considered constant.
        Complexity:
            Time: O(n + m * log(m))
            Space: O(n)
        """
        char_counts_sorted = sorted(Counter(s).items())
        res_char_arr: list[str] = []
        while char_counts_sorted:
            # get lexicographically largest char
            char, count = char_counts_sorted.pop()
            if repeatLimit >= count:
                # fully used up largest char, continue
                res_char_arr.append(char * count)
                continue

            # append `repeatLimit` of largest char to result
            res_char_arr.append(char * repeatLimit)
            if not char_counts_sorted:
                # no more other characters left, can not break the
                # streak of `char` with a different character
                break

            # get the second highest character and append it a single time
            char2, count2 = char_counts_sorted.pop()
            res_char_arr.append(char2)

            # append character occurances back onto stack
            if count2 > 1:
                char_counts_sorted.append((char2, count2 - 1))
            char_counts_sorted.append((char, count - repeatLimit))

        # convert the character array into a string
        return "".join(res_char_arr)
