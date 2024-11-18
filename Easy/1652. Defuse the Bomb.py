"""
You have a bomb to defuse, and your time is running out! Your informer will
provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are
replaced simultaneously.
- If k > 0, replace the ith number with the sum of the next k numbers.
- If k < 0, replace the ith number with the sum of the previous k numbers.
- If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous
element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code
to defuse the bomb!

Constraints:
- n == code.length
- 1 <= n <= 100
- 1 <= code[i] <= 100
- -(n - 1) <= k <= n - 1
"""

import itertools


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # get prefix sums of code, use code twice to acocunt for circular array
        accu = list(itertools.accumulate(itertools.chain(code, code)))
        n = len(code)
        res: list[int] = []
        for i, num in enumerate(code):
            if num == 0:
                res.append(0)
                continue
            # get actual k, as k may be negative and behavior for
            # next and previous k numbers is different
            actual_k = k if num > 0 else -k
            if actual_k >= 0:
                sub_arr_sum = accu[i + actual_k] - accu[i]
            else:
                # add n to indexes to account for loop around
                sub_arr_sum = accu[i + n - 1] - accu[i + n + actual_k - 1]
            res.append(sub_arr_sum)
        return res
