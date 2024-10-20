"""
A boolean expression is an expression that evaluates to either true or false.
It can be in one of the following shapes:
-'t' that evaluates to true.
-'f' that evaluates to false.
-'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
-'&(subExpr_1, subExpr_2,..., subExpr_n)' that evaluates to the logical AND of
the inner expressions subExpr_1, subExpr_2,..., subExpr_n where n >= 1.
-'|(subExpr_1, subExpr_2,..., subExpr_n)' that evaluates to the logical OR of
the inner expressions subExpr_1, subExpr_2,..., subExpr_n where n >= 1.

Given a string expression that represents a boolean expression, return the
evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

Constraints:
- 1 <= expression.length <= 2 * 10^4
- expression[i] is one following characters:'(',')','&','|','!','t','f', and','.
"""

import operator
from typing import Callable, Literal

x = operator.or_


class SolutionBracketBased:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        self.expression = expression
        self.bracket_pairs = self._get_bracket_pairs()
        return self._parseBoolExpr(0)

    def _parseBoolExpr(self, i: int) -> bool:
        """
        Evaluate self.expression starting from index i. End of current sub-expression is implicit.
        """
        match self.expression[i]:
            case "t":
                return True
            case "f":
                return False
            case "!":
                return not self._parseBoolExpr(i + 2)
            case "&":
                return self._evaluate_and_or(i, operator.and_)
            case "|":
                return self._evaluate_and_or(i, operator.or_)
            case _c:
                raise Exception(f"Invalid character encountered: {_c}")

    def _get_bracket_pairs(self) -> dict[int, int]:
        """Generate a mapping of indexes of opening brackets to closing brackets."""
        expression = self.expression
        bracket_pairs: dict[int, int] = {}
        open_bracket_stack: list[int] = []
        for i, c in enumerate(expression):
            if c == "(":
                open_bracket_stack.append(i)
            elif c == ")":
                bracket_pairs[open_bracket_stack.pop()] = i
        return bracket_pairs

    def _evaluate_and_or(self, i: int, _operator: Callable[[int, int], bool]) -> bool:
        """
        Evaluate & or | for self.expression[i:]
        """
        if _operator == operator.or_:
            res = False
        else:
            res = True
        early_exit = not res

        prev_idx = i + 1  # position of opening bracket (will be excluded)
        end_of_operator_bracket = self.bracket_pairs[i + 1]
        while True:
            next_idx = self._find_next_comma_of_bracket(
                prev_idx + 1, end_of_operator_bracket
            )
            if next_idx == -1:
                res = _operator(res, self._parseBoolExpr(prev_idx + 1))
                break
            res = _operator(res, self._parseBoolExpr(prev_idx + 1))
            if res is early_exit:
                return early_exit
            prev_idx = next_idx
        return res

    def _find_next_comma_of_bracket(self, i: int, bracket_end: int) -> int:
        """Find the index of the next comma within the brackets.


        Args:
            i (int): Index of previous comma or opening bracket.
            bracket_end (int): Index of closing bracket.

        Returns:
            int: Index of next comma or -1 if no more commas within brackets.
        """
        expression = self.expression
        while i < bracket_end:
            if expression[i] == ",":
                return i
            if expression[i] == "(":
                i = self.bracket_pairs[i] + 1
            else:
                i += 1
        return -1


class SolutionSimpleStack:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        stack: list[str] = []

        for char in expression:
            if char == ",":
                continue
            elif char == ")":
                # Evaluate the expression within the parentheses
                seen: set[Literal["t", "f"]] = set()
                while stack[-1] != "(":
                    val = stack.pop()
                    assert val == "t" or val == "f"
                    seen.add(val)
                stack.pop()  # Remove the '('

                # Get the operator before the '('
                operator = stack.pop()
                if operator == "&":
                    stack.append("t" if all(c == "t" for c in seen) else "f")
                elif operator == "|":
                    stack.append("t" if any(c == "t" for c in seen) else "f")
                elif operator == "!":
                    stack.append("f" if "t" in seen else "t")
            else:
                # Push the current character onto the stack
                stack.append(char)

        # The final result should be on the top of the stack
        return stack[-1] == "t"


class Solution(SolutionSimpleStack):
    pass
