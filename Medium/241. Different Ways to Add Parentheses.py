from typing import List


class Solution:
    """
    Given a string expression of numbers and operators, return all possible results from computing
    all the different possible ways to group numbers and operators. You may return the answer in
    any order.
    The test cases are generated such that the output values fit in a 32-bit integer and the number
    of different results does not exceed 10^4.
    Constraints:
        1 <= expression.length <= 20
        expression consists of digits and the operator '+', '-', and '*'.
        All the integer values in the input expression are in the range [0, 99].
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # solve recursively, splitting at each operation symbol
        bin_ops = "+-*"

        res = []
        for i, c in enumerate(expression):
            # if character is an operation, split
            if c in bin_ops:
                # find all possible results for each side of expression
                firs_operand_options = self.diffWaysToCompute(expression[:i])
                second_operand_options = self.diffWaysToCompute(expression[i+1:])

                # add to results every possibility of combining the two part results
                if c == '+':
                    res.extend(p1 + p2 for p1 in firs_operand_options for p2 in second_operand_options)
                elif c == '-':
                    res.extend(p1 - p2 for p1 in firs_operand_options for p2 in second_operand_options)
                else:
                    res.extend(p1 * p2 for p1 in firs_operand_options for p2 in second_operand_options)

        # recursion base case: only integer
        if len(res) == 0:
            res.append(int(expression))

        return res
