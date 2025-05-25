"""
Given a string s, find the sum of the 3 largest unique prime numbers that can
be formed using any of its substrings.

Return the sum of the three largest unique prime numbers that can be formed. If
fewer than three exist, return the sum of all available primes. If no prime
numbers can be formed, return 0.

A prime number is a natural number greater than 1 with only two factors, 1 and
itself.

A substring is a contiguous sequence of characters within a string.

Note: Each prime number should be counted only once, even if it appears in
multiple substrings. Additionally, when converting a substring to an integer,
any leading zeros are ignored.

Constraints:
- 1 <= s.length <= 10
- s consists of only digits.
"""


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        """Generate all substrings, check for primeality and sum largest.

        Complexity:
            n = int(s)
            Time: O(s^2 * n^0.5)
            Space: O(s^2 + n^0.5)
        """
        substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        ints = list(set(int(s) for s in substrings))
        primes = self.get_primes(max(ints))
        ints.sort(reverse=True)
        res = 0
        count = 0
        for integer in ints:
            if self.is_prime(integer, primes):
                res += integer
                count += 1
                if count == 3:
                    break
        return res

    def is_prime(self, n: int, primes: list[int]):
        if n == 1:
            return False
        for p in primes:
            if p == n:
                return True
            if not n % p:
                return False
        return True

    def get_primes(self, n: int):
        sqrt_n = int(n**0.5) + 2
        is_prime = [False, True] * ((sqrt_n // 2) + 2)
        primes = [2]
        for i in range(3, sqrt_n, 2):
            if not is_prime[i]:
                continue
            primes.append(i)
            for j in range(i * i, sqrt_n, i):
                is_prime[j] = False
        return primes


def test():
    s = Solution()
    res = s.sumOfLargestPrimes("12234")
    real = 1469
    assert res == real, res
    s.sumOfLargestPrimes("2357975917")


test()
