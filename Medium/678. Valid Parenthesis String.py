"""
Given a string s containing only three types of characters: '(', ')' and '*',
return trueifsis valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left
  parenthesis '(' or an empty string "".

Constraints:
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        # keep stack of not yet closed brackets and asterisks
        opens: list[int] = []
        jokers: list[int] = []
        for i, char in enumerate(s):
            if char == "(":
                opens.append(i)
            elif char == ")":
                # "use up" last unclosed open bracket if it exists
                if len(opens):
                    opens.pop()
                else:
                    # else if none are left, use a joker if any are left
                    if len(jokers):
                        jokers.pop()
                    else:
                        # if none are left, cannot form valid parenthesis string
                        return False
            else:
                jokers.append(i)

        # close any unclosed opening brackets
        if len(opens) > len(jokers):
            # if more unclosed opening brackets than jokers, cannot form valid parenthesis string
            return False
        while opens:
            if opens.pop() > jokers.pop():
                # if an unclosed bracket comes after all unsused jokers, cannot form valid parenthesis string
                return False

        # all parentheses paired up, string is valid
        return True
