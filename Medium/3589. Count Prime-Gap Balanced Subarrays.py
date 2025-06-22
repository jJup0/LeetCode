"""
You are given an integer array nums and an integer k.

A subarray is called prime-gap balanced if:
- It contains at least two prime numbers, and
- The difference between the maximum and minimum prime numbers in that subarray
  is less than or equal to k.

Return the count of prime-gap balanced subarrays in nums.

Note:
- A subarray is a contiguous non-empty sequence of elements within an array.
- A prime number is a natural number greater than 1 with only two factors, 1
  and itself.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 5 * 10^4
- 0 <= k <= 5 * 10^4
"""

from sortedcontainers import SortedList


class Solution:
    def primeSubarray(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        primes: set[int] = set(self._generate_primes(max(nums) + 3))
        # left pointer of current sliding window
        l = 0
        res = 0
        # sorted list of primes in current sliding window
        curr_primes: SortedList[int] = SortedList()
        # indexes of the two last primes
        second_last_prime_idx = last_prime_idx = -1
        for r, num in enumerate(nums):
            is_prime = num in primes
            if is_prime:
                curr_primes.add(num)

            if len(curr_primes) >= 2:
                # shrink window from left while largest difference
                # between primes is larger than k
                while curr_primes[-1] - curr_primes[0] > k:
                    if nums[l] in primes:
                        curr_primes.remove(nums[l])
                    l += 1

            if len(curr_primes) >= 2:
                # current sliding window is valid
                if is_prime:
                    # if current number is prime, then all subarrays ending with
                    # current number and starting from left to last prime are valid
                    res += last_prime_idx - l + 1
                else:
                    # if current number is not prime, then we can skrink subarray
                    # to second last prime and all those subarrays are valid
                    res += second_last_prime_idx - l + 1

            if is_prime:
                second_last_prime_idx = last_prime_idx
                last_prime_idx = r

        return res

    def _generate_primes(self, n: int) -> list[int]:
        if n < 2:
            return []
        is_prime = [False, True] * ((n // 2) + 1)
        primes = [2]
        for i in range(3, n + 1, 2):
            if not is_prime[i]:
                continue
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        return primes


def test():
    s = Solution()
    res = s.primeSubarray([41543, 45757, 23773], 26643)
    real = 3
    assert res == real, res

    res = s.primeSubarray([9551, 41039, 4411], 41466)
    real = 2
    assert res == real, res


test()
