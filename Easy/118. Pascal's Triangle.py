class Solution:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

    Constraints:
    - 1 <= numRows <= 30
    """

    def generate(self, numRows: int) -> list[list[int]]:
        """
        O(n^2) / O(n^2)     time / space complexity
        """
        pascal: list[list[int]] = []
        prev_level: list[int] = []
        for i in range(numRows):
            curr_level = prev_level.copy()
            for j in range(1, i):
                # add previous result row shifted to left by one cell to current
                # level (which is a copy)
                curr_level[j] += prev_level[j - 1]
            curr_level.append(1)

            pascal.append(curr_level)
            prev_level = curr_level

        return pascal
