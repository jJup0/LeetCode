"""
Given a string expression representing an expression of fraction addition and
subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an
integer, change it to the format of a fraction that has a denominator 1. So in
this case, 2 should be converted to 2/1.

Constraints:
- The input string only contains'0' to'9','/','+' and'-'. So does the output.
- Each fraction (input and output) has the format ±numerator/denominator. If
  the first input fraction or the output is positive, then'+' will be omitted.
- The input only contains valid irreducible fractions, where the numerator and
  denominator of each fraction will always be in the range [1, 10]. If the
  denominator is 1, it means this fraction is actually an integer in a fraction
  format defined above.
- The number of given fractions will be in the range [1, 10].
- The numerator and denominator of the final result are guaranteed to be valid
  and in the range of 32-bit int.
"""

import itertools
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # convert every fraction to lcm version
        lcm = math.lcm(*range(2, 11))
        # current numerator of total sum of all fractions so far, with lcm as the denominator
        total_in_lcm = 0

        if expression[0] != "-":
            # prepend implicit "+" to first fraction, terrible waste of computational power, but this is python
            expression = "+" + expression
        # split expression into fraction chunks
        add_minus_idxs = [
            i for i, char in enumerate(expression) if char == "-" or char == "+"
        ]
        # add dummy sign at the end of list to properly use itertools.pairwise
        add_minus_idxs.append(len(expression))

        # iterate over each chunk
        for chunk_start, chunk_end in itertools.pairwise(add_minus_idxs):
            sign = expression[chunk_start]
            numerator_str, denominator_str = expression[
                chunk_start + 1 : chunk_end
            ].split("/")
            # convert the fraction into lcm(1..10) version
            numerator_in_lcm = int(numerator_str) * (lcm // int(denominator_str))
            if sign == "+":
                total_in_lcm += numerator_in_lcm
            else:
                total_in_lcm -= numerator_in_lcm

        # simplify fraction by dividing by greatest common divisor
        gcd_of_result = math.gcd(total_in_lcm, lcm)
        return f"{total_in_lcm//gcd_of_result}/{lcm//gcd_of_result}"
