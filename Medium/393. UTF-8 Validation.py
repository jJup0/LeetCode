from typing import List


class Solution:
    """
    Given an integer array data representing the data, return whether it is a valid UTF-8 encoding
    (i.e. it translates to a sequence of valid UTF-8 encoded characters).

    A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

    For a 1-byte character, the first bit is a 0, followed by its Unicode code.
    For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1
    bytes with the most significant 2 bits being 10.
    This is how the UTF-8 encoding would work:

        Number of Bytes    |        UTF-8 Octet Sequence
                           |              (binary)
    -----------------------+-----------------------------------------
                1          |   0xxxxxxx
                2          |   110xxxxx 10xxxxxx
                3          |   1110xxxx 10xxxxxx 10xxxxxx
                4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    x denotes a bit in the binary form of a byte that may be either 0 or 1.

    Note: The input is an array of integers. Only the least significant 8 bits of each integer is
    used to store the data. This means each integer represents only 1 byte of data.
    Constraints:
        1 <= data.length <= 2 * 10^4
        0 <= data[i] <= 255
    """

    def validUtf8(self, data: List[int]) -> bool:
        l = len(data)

        # bit masks for checking validity
        one_one = 196
        one_zero = 128

        # iterate through data
        i = 0
        while i < l:
            # find first unset bit
            d = data[i]
            for fbc in range(7, 2, -1):
                if not (d & (1 << fbc)):
                    break
            # more than 4 leading 1's
            else:
                return False

            # one byte word, with leading zero; valid
            if fbc == 7:
                i += 1
                continue

            # leading bit is set, second highest is cleared, invalid as starting byte
            if fbc == 6:
                return False

            # byte length of utf-8 character
            wlen = 7 - fbc

            # not enough bytes left in data array
            if i + wlen > l:
                return False

            for i in range(i + 1, i + wlen):
                first_two_bits = data[i] & one_one
                if first_two_bits < one_zero or first_two_bits == one_one:
                    # follow up byte not 10xxxxxx
                    return False
            i += 1

        # if no rules were broken, return True
        return True
