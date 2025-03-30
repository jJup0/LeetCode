"""
You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by
applying the following operation at most k times:
- Choose any non-empty subarray nums[l,..., r] that you haven't chosen previously.
- Choose an element x of nums[l,..., r] with the highest prime score. If
  multiple such elements exist, choose the one with the smallest index.
- Multiply your score by x.

Here, nums[l,..., r] denotes the subarray of nums starting at index l and
ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime
factors of x. For example, the prime score of 300 is 3 since
300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= nums.length == n <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= min(n * (n + 1) / 2, 10^9)
"""


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n^1.5 / log(n))
            Space: O(n)
        """
        MOD = 10**9 + 7

        primes = self._get_primes(max(nums))
        prime_scores = self._get_prime_scores(nums, primes)
        dominant_intervals = self._get_dominant_areas(prime_scores)

        nums_sorted = sorted(((num, i) for i, num in enumerate(nums)), reverse=True)
        res = 1
        operations_remaining = k
        # iterate through numbers in reverse sorted order
        for num, i in nums_sorted:
            dominant_left, dominant_right = dominant_intervals[i]
            # number of subarrays where nums[i] has the highest primes score
            ways = (i - dominant_left + 1) * (dominant_right - i + 1)
            if ways >= operations_remaining:
                # use up the rest of k
                res = (res * pow(num, operations_remaining, MOD)) % MOD
                break
            # use all subarrays possible and multiply them to result
            res = (res * pow(num, ways, MOD)) % MOD
            operations_remaining -= ways
        return res

    def _get_prime_scores(self, nums: list[int], primes: list[int]):
        """Calculate the prime score for each number in nums.

        Complexity:
            Time: O(n^1.5 / log(n))
            Space: O(n)
        """
        primes_set = frozenset(primes)
        prime_scores: list[int] = []
        for num in nums:
            score = 0
            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    score += 1
                    while num % prime == 0:
                        num //= prime
            if num in primes_set:
                score += 1
            prime_scores.append(score)
        return prime_scores

    def _get_primes(self, n: int):
        """Get primes up to n.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        is_prime = [False, True] * (n + 1)
        primes = [2]
        for i in range(3, n + 1, 2):
            if not is_prime[i]:
                continue
            primes.append(i)
            for j in range(i * i, n, i):
                is_prime[j] = False
        return primes

    def _get_dominant_areas(self, prime_scores: list[int]):
        """
        For each score in primes scores get an interval [l, r] (inclusive)
        of the largest subarray for which is is the largest with the smallest
        index.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        res: list[tuple[int, int]] = [(-1, -1)] * len(prime_scores)
        # monotone stack for decreasing index score
        # each element looks like: (score, index in res, start)
        monotone_stack: list[tuple[int, int, int]] = []
        for i, score in enumerate(prime_scores):
            # pop all smaller prime scores from stack and set
            # its dominant interval in `res`
            while monotone_stack and monotone_stack[-1][0] < score:
                _s, j, start = monotone_stack.pop()
                res[j] = (start, i - 1)

            if monotone_stack:
                # if stack is not empty then stack[-1] is the last primescore
                # that is greater equal the current prime score, so append
                # its index + 1 as the lower bound of its dominant interval
                monotone_stack.append((score, i, monotone_stack[-1][1] + 1))
            else:
                # largest score so far, its dominant interval starts at 0
                monotone_stack.append((score, i, 0))
        # write to result for res of the stack
        for _s, j, start in monotone_stack:
            res[j] = (start, len(prime_scores) - 1)
        return res


def test():
    s = Solution()
    res = s.maximumScore([8, 3, 9, 3, 8], 2)
    assert res == 81
    res = s.maximumScore([19, 12, 14, 6, 10, 18], 3)
    assert res == 4788
    res = s.maximumScore([1, 7, 11, 1, 5], 14)
    assert res == 823751938


test()
