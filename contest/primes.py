class Solution:
    def yield_primes_infinite(self):
        """
        Sieve of Eratosthenes
        Code by David Eppstein, UC Irvine, 28 Feb 2002
        http://code.activestate.com/recipes/117119/

        Generate an infinite sequence of prime numbers.
        """
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        divisors: dict[int, list[int]] = {}

        for num in range(2, 1 << 63):
            if num not in divisors:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                yield num
                divisors[num * num] = [num]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                for prime_divisor in divisors.pop(num):
                    divisors.setdefault(prime_divisor + num, []).append(prime_divisor)

    def generate_primes(self, n: int) -> list[int]:
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

    def is_prime(self, n: int) -> bool:
        """Miller-rabin primeality test."""
        # small_witness_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] # for 2**64
        small_witness_primes = [2, 7, 61]  # for 2**32
        if n < 2:
            return False

        # check is small primes divide n or n is small prime
        for p in small_witness_primes:
            if n % p == 0:
                return n == p

        # write n-1 as d*2^s, where d is odd
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        for a in small_witness_primes:
            if a >= n:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True


def test():
    def test_all_equal(n: int):
        sol = Solution()
        primes1 = sol.generate_primes(n)

        prime_yielder = sol.yield_primes_infinite()
        primes2: list[int] = []
        while not primes2 or primes2[-1] <= n:
            primes2.append(next(prime_yielder))
        primes2.pop()

        primes3 = [i for i in range(1, n + 1) if sol.is_prime(i)]

        assert primes1 == primes2, f"{n=} {primes1=} {primes2=}"
        assert primes2 == primes3, f"{n=} {primes2=} {primes3=}"

    for i in range(20):
        test_all_equal(i)
    test_all_equal(100000)


test()
