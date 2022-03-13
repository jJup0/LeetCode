class Solution:
    def isValid(self, s: str) -> bool:
        # keeps a stack of open brackets
        bracket_stack = [' ']
        # opening bracket to closing bracket map
        open_to_close = {
            '(': ')',
            '[': ']',
            '{': '}',
            ' ': None
        }

        for c in s:
            # opening brackets always allowed, append to stack
            if c in open_to_close:  # currently opening
                bracket_stack.append(c)
            # if closing bracket, check if its closing the last open bracket
            # if not return false
            elif c != open_to_close[bracket_stack.pop()]:
                return False

        # if stack == [' '] at the end, then return true
        # otherwise still unclosed brackets and return false
        return len(bracket_stack) == 1
