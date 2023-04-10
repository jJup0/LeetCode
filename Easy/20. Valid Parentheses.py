class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

    Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.
    """

    def isValid(self, s: str) -> bool:
        """
        Iterates through string keeping stack of open parentheses.
        O(n) / O(n)     time / space complexity
        """

        # stack of open parentheses
        stack = []

        # strings containing opening and closing parentheses
        opening = "([{"
        closing = ")]}"
        for parenthesis in s:
            if parenthesis in opening:
                stack.append(parenthesis)
            else:
                # if stack is empty and parenthesis is closing, then sequence is not valid
                if not stack:
                    return False
                opening_parenthesis = stack.pop()
                # if closing parenthesis does not match most recent
                # unclosed parenthesis then sequence is not valid
                if opening.index(opening_parenthesis) != closing.index(parenthesis):
                    return False

        # all open parentheses must be closed
        return len(stack) == 0
