"""
A sentence is a list of words that are separated by a single space with no
leading or trailing spaces.
- For example,"Hello World","HELLO","hello world hello world" are all sentences.

Words consist of only uppercase and lowercase English letters. Uppercase and
lowercase English letters are considered different.

A sentence is circular if:
- The last character of a word is equal to the first character of the next word.
- The last character of the last word is equal to the first character of the
  first word.

For
example,"leetcode exercises sound delightful","eetcode","leetcode eats soul"
are all circular sentences.
However,"Leetcode is cool","happy Leetcode","Leetcode" and"I like Leetcode" are
not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

Constraints:
- 1 <= sentence.length <= 500
- sentence consist of only lowercase and uppercase English letters and spaces.
- The words in sentence are separated by a single space.
- There are no leading or trailing spaces.
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        for i in range(1, len(sentence) - 1):
            if sentence[i] == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False
                i += 2
            else:
                i += 1
        return sentence[0] == sentence[-1]
