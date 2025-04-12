"""
You are given two positive integers n and k.

An integer x is called k-palindromic if:
- x is a palindrome.
- x is divisible by k.

An integer is called good if its digits can be rearranged to form a
k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form
the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a
k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after
rearrangement. For example, 1010 cannot be rearranged to form 101.

Constraints:
- 1 <= n <= 10
- 1 <= k <= 9
"""

import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        """Stolen and refactored from LeetCode editorial.

        Complexity:
            m := n // 2
            Time: O(n * log(n) * 10**m)
            Space: O(n * 10**m)
        """
        unique_palindromes = self._get_canonical_palindromes(n, k)
        return self._calculate_unique_permutations(n, unique_palindromes)

    def _get_canonical_palindromes(self, n: int, k: int):
        # set of palidromic numbers sorted by digits
        canonical_palindrome_digits: set[str] = set()
        power_10_half = 10 ** ((n - 1) // 2)
        palindrome_odd_length = n & 1
        # enumerate all palindrome numbers with n digits divisible by k
        for num in range(power_10_half, power_10_half * 10):
            str_num = str(num)
            palindrome_str = str_num + str_num[::-1][palindrome_odd_length:]
            if int(palindrome_str) % k == 0:
                # sort digits to create canonical version of palindromic numbers
                sorted_digits = "".join(sorted(palindrome_str))
                canonical_palindrome_digits.add(sorted_digits)
        return canonical_palindrome_digits

    def _calculate_unique_permutations(self, n: int, unique_palindromes: set[str]):
        factorials = [math.factorial(i) for i in range(n + 1)]
        res = 0
        for num_str in unique_palindromes:
            # counter of digits in number
            digit_count = [0] * 10
            for c in num_str:
                digit_count[int(c)] += 1

            # calculate unique permutations of the multiset of digits
            # fix first number to be non 0, then permute the rest of
            # the digits to exlude permutations starting with 0
            permutations = (n - digit_count[0]) * factorials[n - 1]
            for x in digit_count:
                permutations //= factorials[x]
            res += permutations
        return res
