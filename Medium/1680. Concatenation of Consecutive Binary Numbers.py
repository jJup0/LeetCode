class Solution:
    """
    Given an integer n, return the decimal value of the binary string formed by concatenating the
    binary representations of 1 to n in order, modulo 10^9 + 7.
    Constraints:
        1 <= n <= 10^5
    """

    def concatenatedBinary(self, n: int) -> int:
        """
        Vitually concatenate binary representation by shifting previous result by bit length.
        O(n) / O(1)     time / space complexity
        """

        MOD = 1_000_000_007
        x = 0
        for i in range(1, n + 1):
            x = ((x << i.bit_length()) + i) % MOD
        return x

    def concatenatedBinary_no_bitlength(self, n: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """

        MOD = 1_000_000_007
        x = 0
        power_of_2 = 2
        for i in range(1, n + 1):
            # every time new power of two is reached, update power of two to vitually bitshift x
            # by the correct amount
            if i == power_of_2:
                power_of_2 <<= 1
            x = ((x * power_of_2) + i) % MOD
        return x

    def concatenatedBinary_string(self, n: int) -> int:
        """
        Apparantly bitshift work around is slower ok sorry boss
        O(n) / O(n)     time / space complexity
        """
        # first build f string to be filled with n integers in binary
        # format this string with the numbers [1:n] inclusive
        s = ('{:b}' * n).format(*range(1, n + 1))

        # convert to int and take modulo
        return int(s, 2) % (10 ** 9 + 7)


    # cracked answer idk boss, explanation was terrible
    # # def concatenatedBinary2(self, n):
    # #     def bin_pow(num):
    # #         return [1 << i for i, b in enumerate(bin(num)[:1:-1]) if b == "1"]

    # #     ans, MOD, q = 0, 10**9 + 7, len(bin(n)) - 3

    # #     B = bin_pow((1 << q) - 1) + bin_pow(n - (1 << q) + 1)[::-1]
    # #     C = list(range(1, q+1)) + [q+1]*(len(B) - q)
    # #     D = list(accumulate(i*j for i, j in zip(B[::-1], C[::-1])))[::-1][1:] + [0]

    # #     for a, b, c, d in zip(accumulate(B), B, C, D):
    # #         t1 = pow(2, b*c, MOD) - 1
    # #         t2 = pow(pow(2, c, MOD)-1, MOD - 2, MOD)
    # #         ans += t2*((a-b+1+t2)*t1-b)*pow(2, d, MOD)

    # #     return ans % MOD

    # apparantly matrix multiplication solution exists as well, but couldnt find good explanation either
