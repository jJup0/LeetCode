from typing import List


class Solution:
    """
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
    Note that division between two integers should truncate toward zero.
    It is guaranteed that the given RPN expression is always valid. That means the
    expression would always evaluate to a result, and there will not be any division by zero operation.
    Constraints:
        1 <= tokens.length <= 10^4
        tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
    """

    def evalRPN(self, tokens: List[str]) -> int:
        # uses Python 3.10 match syntax

        # operands stack
        stack = []
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

        # if input is correct, one "operand" will remain
        assert len(stack) == 1
        return stack[0]
