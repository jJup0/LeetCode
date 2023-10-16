class Solution:
    """
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
    Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above it as shown:

    Constraints:
    - 0 <= rowIndex <= 33
    """

    def getRow(self, row_index: int) -> list[int]:
        # pre calculate factorials
        factorials = [1] * (row_index + 1)
        for i in range(1, len(factorials)):
            factorials[i] = factorials[i - 1] * i

        # left half of result list
        result_left = [-1] * ((row_index + 2) // 2)
        for i in range((row_index + 2) // 2):
            # pascals triangle is just n choose k, where n is the row_index
            # and k is the index within that row
            result_left[i] = int(
                factorials[row_index] / (factorials[i] * factorials[row_index - i])
            )

        if row_index % 2:
            # for even index just duplicate, reverse and append to result
            return result_left + result_left[::-1]

        # for odd index, do not include last value, as this is the middle value
        # in the final result and only appears once
        return result_left + result_left[-2::-1]
