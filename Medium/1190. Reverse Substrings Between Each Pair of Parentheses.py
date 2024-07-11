"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the
innermost one.

Your result should not contain any brackets.

Constraints:
- 1 <= s.length <= 2000
- s only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        Keep stack of chars between parentheses that have not been converted yet.
        O(n^2) / O(n)       time / space complexity
        """
        stack: list[str] = []
        for c in s:
            if c != ")":
                stack.append(c)
                continue

            chars_in_reverse: list[str] = []
            while stack[-1] != "(":
                chars_in_reverse.append(stack.pop()[::-1])
            stack[-1] = "".join(chars_in_reverse)
        return "".join(stack)
