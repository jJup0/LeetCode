from typing import List


class Solution:
    """
    You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each
    index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of
    nums starting at i (inclusive) that has the maximum possible bitwise OR.
    In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the
    smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik)
    where i <= k <= n - 1.
    The bitwise OR of an array is the bitwise OR of all the numbers in it.
    Return an integer array answer of size n where answer[i] is the length of the minimum sized
    subarray starting at i with maximum bitwise OR.
    A subarray is a contiguous non-empty sequence of elements within an array.
    Constraints:
        n == nums.length
        1 <= n <= 10^5
        0 <= nums[i] <= 10^9
    """

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        Original from contest. b = maximum bit length
        O(n * b) / O(n + b)     time / space complexity
        """

        n = len(nums)

        # find the max OR for each i, 0 <= i < n
        x = 0
        max_or = []
        for num in reversed(nums):
            x |= num
            max_or.append(x)
        max_or = max_or[::-1]

        # result variable
        res = []

        # current stacked counts for each bit for subarray nums[i:j]
        bits = [0] * max(1, max_or[0].bit_length())
        j = 0
        for i in range(n):
            # convert max_or[i] into bit array
            bits_needed = [int(b) for b in bin(max_or[i])[2:][::-1]]
            # iterate through needed bits
            for bni in range(len(bits_needed)):
                # if current bits == 0 and bits_needed == 1, add nums[j] to subarray
                while bits[bni] < bits_needed[bni] and j < n:
                    # add bit representation of nums[j] to bits
                    new_bits = [int(b) for b in bin(nums[j])[2:][::-1]]
                    for k in range(len(new_bits)):
                        bits[k] += new_bits[k]
                    j += 1

            # append interval length to result, if filled with zeroes will be negative, so minimum of 1
            res.append(max(1, j-i))

            # subtract nums[i] from current bit counts
            to_remove = [int(b) for b in bin(nums[i])[2:][::-1]]
            for k in range(len(to_remove)):
                bits[k] -= to_remove[k]

        return res
