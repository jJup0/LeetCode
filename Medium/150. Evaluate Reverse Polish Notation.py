"""
You are given an array of strings tokens that represents an arithmetic
expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the
expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a
  32-bit integer.

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
  range [-200, 200].
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # operands stack
        stack: list[int] = []
        for token in tokens:
            # any binary operation works on the top two items in the stack, i.e
            # consumes the top operand and applies it to the new top operand
            match token:
                case "+":
                    add = stack.pop()
                    stack[-1] += add
                case "-":
                    sub = stack.pop()
                    stack[-1] -= sub
                case "*":
                    mult = stack.pop()
                    stack[-1] *= mult
                case "/":
                    divisor = stack.pop()
                    stack[-1] = int(stack[-1] / divisor)
                case _:
                    # if the token is not an operation, it is an integer, so append it to the operands stack
                    stack.append(int(token))

        # if input is correct, one operand will remain
        assert len(stack) == 1
        return stack[0]
