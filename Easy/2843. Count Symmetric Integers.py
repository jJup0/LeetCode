"""
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n
digits of x is equal to the sum of the last n digits of x. Numbers with an odd
number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

Constraints:
- 1 <= low <= high <= 10^4
"""

from functools import cache
from typing import Any, Generator


class Solution3:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """Fastest, general implementation for arbitrary low and high.

        Complexity:
            Time: O(sqrt(n))
            Space: O(log(n)^2)
        """
        res = 0
        # amount of digits to mirror, i.e. digit_mirror_count=2 means four digit numbers
        for digit_mirror_count in range(1, len(str(high))):
            power_10 = 10**digit_mirror_count
            if power_10 * power_10 < low:
                # largest symmetric integer for this order of magnitude lower than low, skip
                continue

            # smallest number to use as lower digits
            higher_digits_low = self._bin_search_for_lowest_digits(low, power_10)

            for digits_left in range(higher_digits_low, power_10):
                number_left = digits_left * power_10

                # sum of digits in the left half of the number
                digit_sum = self._get_sum_digits(digits_left)

                highest_possible_num = number_left + power_10 - 1
                if low <= number_left and highest_possible_num <= high:
                    # all symmetric numbers starting with `digits_left` are in
                    # the range [low, high], simply add the count
                    res += self._gen_digits_count(digit_sum, digit_mirror_count + 1)
                    continue

                # manually iterate through symmetric integers until upper bound reached
                for digits_right in self._generate_digits(
                    digit_sum, digit_mirror_count + 1
                ):
                    num = number_left + digits_right
                    if num < low:
                        continue
                    if num > high:
                        return res
                    res += 1
        return res

    def _bin_search_for_lowest_digits(self, low: int, power_10: int):
        smaller_power_10 = power_10 // 10
        if low <= (smaller_power_10 + 1) * power_10 - 1:
            return smaller_power_10

        higher_digits_low = smaller_power_10
        higher_digits_high = power_10
        while higher_digits_low < higher_digits_high:
            mid = (higher_digits_low + higher_digits_high) // 2

            num_l = mid * power_10
            highest_possible_num = num_l + power_10 - 1
            if highest_possible_num < low:
                higher_digits_low = mid + 1
            else:
                higher_digits_high = mid
        return higher_digits_low

    def _get_sum_digits(self, digits: int):
        digit_sum = 0
        digits_copy = digits
        while digits_copy:
            digits_copy, digit = divmod(digits_copy, 10)
            digit_sum += digit
        return digit_sum

    def _generate_digits(
        self, digit_sum: int, length: int
    ) -> Generator[int, Any, None]:
        """Generate numbers whose digits some up to `digit_sum` and have `length` digits, leading zeros allowed."""
        if length == 1:
            yield digit_sum
            return

        power_10 = 10 ** (length - 1)
        smallest = max(0, digit_sum - ((length - 1) * 9))
        for digit in range(smallest, min(digit_sum, 9) + 1):
            for lower_digits in self._generate_digits(digit_sum - digit, length - 1):
                full_num = digit * power_10 + lower_digits
                yield full_num

    @cache
    def _gen_digits_count(self, digit_sum: int, num_digits: int) -> int:
        """Calculates the amount of numbers yielded by _generate_digits(digit_sum, length)."""
        if num_digits == 1:
            return 1

        smallest_digit_possible = max(0, digit_sum - ((num_digits - 1) * 9))
        return sum(
            self._gen_digits_count(digit_sum - i, num_digits - 1)
            for i in range(smallest_digit_possible, min(digit_sum, 9) + 1)
        )


class Solution2:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """Faster, integer only calculation.

        Complexity:
            Time: O(high-low * log(high-low))
            Space: O(log(high-low))
        """
        res = 0
        for digits in range(1, 10):
            num = digits * 11
            if num < low:
                continue
            if num > high:
                return res
            res += 1

        for digits_l in range(10, 100):
            thousands, hundreds = divmod(digits_l, 10)
            digit_sum = thousands + hundreds
            num_l = digits_l * 100
            for tens in range(max(0, digit_sum - 9), min(digit_sum, 9) + 1):
                units = digit_sum - tens
                num = num_l + tens * 10 + units
                if num < low:
                    continue
                if num > high:
                    return res
                res += 1
        return res


class Solution1:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """Naive string conversion.

        Complexity:
            Time: O(high-low * log(high-low))
            Space: O(log(high-low))
        """
        res = 0
        for num in range(low, high + 1):
            str_num = str(num)
            if len(str_num) & 1:
                continue
            l = sum(map(int, str_num[: len(str_num) // 2]))
            r = sum(map(int, str_num[len(str_num) // 2 :]))
            res += l == r
        return res


class Solution(Solution3):
    pass


def test_digit_count():
    import random

    sol = Solution()
    max_digits = 5
    for i in range(1000):
        digit_sum = random.randint(1, 9 * max_digits)
        num_digits = random.randint(digit_sum // 9 + 1, max_digits + 1)
        real = sum(1 for _ in sol._generate_digits(digit_sum, num_digits))  # type: ignore
        calced = sol._gen_digits_count(digit_sum, num_digits)  # type: ignore
        assert real == calced
        if not i % 100:
            print(f"{i=}")


def test():
    import random
    import time
    from typing import Any, Callable

    def time_func(func: Callable[[], Any], description: str = "") -> Any:
        t1 = time.perf_counter_ns()
        res = func()
        t2 = time.perf_counter_ns()
        print(f"{(t2 - t1)/1_000_000:.2f}ms for {description}")
        return res

    sol3 = Solution3()
    max_n = 10**7
    random.seed(1)
    for _ in range(5):
        low = random.randint(1, max_n)
        higher_than_root = random.randint(1, 100)
        high = random.randint(1, max_n * higher_than_root * higher_than_root)

        # real = time_func(lambda: s.countSymmetricIntegers1(low, high), "naive")
        res = time_func(lambda: sol3.countSymmetricIntegers(low, high), "v3")
        print(sol3._gen_digits_count.cache_info())  # type: ignore
        print(res)
        # assert res == real


# test_digit_count()
test()
