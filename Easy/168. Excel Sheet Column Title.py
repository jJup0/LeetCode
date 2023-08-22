class Solution:
    """
    Given an integer columnNumber, return its corresponding column title as it
    appears in an Excel sheet.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

    Constraints:
    1 <= columnNumber <= 2^31 - 1
    """

    ord_A = ord("A")

    def convertToTitle(self, column_nr: int) -> str:
        """
        O(log(n)) / O(log(n))   time / space complexity
        """

        res: list[str] = []
        while column_nr > 0:
            # decrement due to weird 1-index based alphabet
            column_nr -= 1
            # calculate character, simply by modulo and adding to chr("A")
            res.append(chr(self.ord_A + (column_nr % 26)))
            # divide by 26 to calculate next order character
            column_nr //= 26

        # column letters are calculated right to left, so reverse list and join
        return "".join(res[::-1])
