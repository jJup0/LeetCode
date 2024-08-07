"""
Convert a non-negative integer num to its English words representation.

Constraints:
- 0 <= num <= 2^31 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        """
        O(log(n)) / O(log(n))   time / space complexity
        """
        # special case, zero
        if num == 0:
            return "Zero"

        powers_of_thousand = {
            1_000_000_000: "Billion",
            1_000_000: "Million",
            1_000: "Thousand",
            1: "",  # pseudo power of ten
        }

        units = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        # word array of result
        res: list[str] = []
        for p10_val, verbose in powers_of_thousand.items():
            if num < p10_val:
                continue

            # extract highest 3 digits of current thousands
            high_digits, num = divmod(num, p10_val)

            # verbosify hundreds first
            if high_digits >= 100:
                res.append(units[high_digits // 100])
                res.append("Hundred")
                high_digits %= 100

            # verbosify tens
            if high_digits >= 20:
                res.append(tens[high_digits // 10])
                high_digits %= 10
            elif high_digits >= 10:
                res.append(teens[high_digits])
                high_digits = 0

            # verbosify units
            if high_digits:
                res.append(units[high_digits])

            # add current thousands as string to word array, do not include empty string
            if verbose:
                res.append(verbose)

        # join prelimary result with spaces
        return " ".join(res)
