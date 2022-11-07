class Solution:
    """
    You are given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9
    becomes 6).

    Constraints:
        1 <= num <= 104
        num consists of only 6 and 9 digits.
    """

    def maximum69Number(self, num: int) -> int:
        # mask to check digits
        mask = 1000
        while mask:
            # if current digit is a 6, replace with a 9 and break
            if (num // mask) % 10 == 6:
                num += 3 * mask
                break

            # reduce mask by factor of 10 to inspect next digit
            mask //= 10

        return num

    def maximum69Number_string_manipulation(self, num: int) -> int:
        c_arr = list(str(num))
        for i, val in enumerate(c_arr):
            if val == '6':
                c_arr[i] = '9'
                break
        return int(''.join(c_arr))
