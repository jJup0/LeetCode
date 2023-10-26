"""
Given an array of unique integers, arr, where each integer arr[i] is strictly
greater than 1.

We make a binary tree using these integers, and each number may be used for any
number of times. Each non-leaf node's value should be equal to the product of
the values of its children.

Return the number of binary trees we can make. The answer may be too large so
return the answer modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 1000
- 2 <= arr[i] <= 10^9
- All the values of arr are unique.
"""
import math


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        """Simple combinatorics.
        O(n^2) / O(n)   time / space complexity
        """
        MOD = 10**9 + 7
        # sort the array to make searching for factors more efficient
        arr.sort()
        # ways to make previous (smaller) numbers, mapping from index to
        ways: dict[int, int] = {}
        for i, num in enumerate(arr):
            # ways to make current number, there is always at least one,
            # where the number makes up the entierty of the binary tree
            curr_ways = 1
            # store square root of current number
            num_sqrt = math.isqrt(num)
            # iterate through all smaller numbers
            for j in range(i):
                potential_factor = arr[j]
                # if the previous number is larger than the square root of the
                # current number, break, as we will get no new factorizations
                if potential_factor > num_sqrt:
                    break
                # if the number is not divisible by the smaller number, continue
                if num % potential_factor:
                    continue

                # calculate the other factor
                other_factor = num // potential_factor
                if other_factor in ways:
                    # there are ways[potential_factor] * ways[other_factor] ways to
                    # build a binary tree with `potential_factor` as the left child
                    # and `other_factor` as the right child
                    combination = ways[potential_factor] * ways[other_factor]
                    if other_factor == potential_factor:
                        # if the other factor is a square, then only add once
                        curr_ways += combination
                    else:
                        # if the other factor is a square, then add twice, as the children can be swapped around
                        curr_ways += combination * 2

            # take number of ways modulo
            ways[num] = curr_ways % MOD

        # return sum of all ways
        return sum(ways.values()) % MOD
