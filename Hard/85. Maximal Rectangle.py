class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """
        O(n * m) / O(n * m)     time / space complexity
        """
        m_width = len(matrix[0])
        # current height of all columns, padd with extra 0 at the end
        heights = [0] * (m_width + 1)
        res = 0
        for row in matrix:
            # update heights, increment if a 1, reset to 0 if a 0
            for j in range(m_width):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0

            # stack of column indices, with monotone increasing height
            # -1 at bottom of the stack acts as height 0 and conveniently also
            # as a pseudo column index that comes before 0 when calaculating
            # widths of rectangles
            stack = [-1]
            for j in range(m_width + 1):
                while heights[j] < heights[stack[-1]]:
                    # use minimum of heights for span of rectangle, which it the column at the top of the stack
                    h = heights[stack.pop()]
                    # use stack[-1] as starting column (or column before starting column) of current rectangle,
                    # and not the column used to pop, since there may be gaps in the indexes in the stack
                    w = j - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(j)
        return res
