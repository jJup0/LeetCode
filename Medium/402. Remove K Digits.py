"""
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Constraints:
- 1 <= k <= num.length <= 10^5
- num consists of only digits.
- num does not have any leading zeros except for the zero itself.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        O(n) / O(n)     time / space complexity
        """
        # convert to char array for O(1) deletions
        num_l = list(num)
        # monotone stack of largest digits and their index
        # bottom entry is a dummy and will never be popped, prevents need for empty check
        largest_digits_pos: list[tuple[int, int]] = [(0, -1)]
        i = 0
        while i < len(num_l) and k > 0:
            if not num_l[i]:
                # deleted previously
                i += 1
                continue

            curr_digit = int(num_l[i])
            if curr_digit >= largest_digits_pos[-1][0]:
                # if digit is largest or equal to unpopped digit so far, add it to the stack
                largest_digits_pos.append((curr_digit, i))
                i += 1
            else:
                # else delete the previous largest digit
                num_l[largest_digits_pos.pop()[1]] = ""
                k -= 1

        # remove leading zeros
        strip_i = 0
        for strip_i, d in enumerate(num_l):
            if d and d != "0":
                break
        # remove digits if any are left
        res = "".join(num_l[strip_i:])
        if k:
            # cut off digits if k remaining
            res = res[:-k]
        return res or "0"
