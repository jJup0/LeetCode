import heapq


class Solution:
    """
    There is a 1-based binary matrix where 0 represents land and 1 represents
    water. You are given integers row and col representing the number of rows
    and columns in the matrix, respectively.

    Initially on day 0, the entire matrix is land. However, each day a new cell
    becomes flooded with water. You are given a 1-based 2D array cells, where
    cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row
    and cith column (1-based coordinates) will be covered with water
    (i.e., changed to 1).

    You want to find the last day that it is possible to walk from the top to the
    bottom by only walking on land cells. You can start from any cell in the top
    row and end at any cell in the bottom row. You can only travel in the four
    cardinal directions (left, right, up, and down).

    Return the last day where it is possible to walk from the top to the bottom
    by only walking on land cells.

    Constraints:
    - 2 <= row, col <= 2 * 10^4
    - 4 <= row * col <= 2 * 10^4
    - cells.length == row * col
    - 1 <= ri <= row
    - 1 <= ci <= col
    - All the values of cells are unique.
    """

    def latestDayToCross(
        self, row_count: int, column_count: int, cells: list[list[int]]
    ) -> int:
        # setup matrix for what cell is blocked on what day
        # pad the matrix on the left, top, and right with 0s
        matrix = [[0] * (column_count + 2) for _ in range(row_count + 1)]
        for _negated_day, (i, j) in enumerate(cells):
            matrix[i][j] = _negated_day

        # setup a matrix for the last possible day for which a cell can still be reached
        # pad the left, top and right with an impossibly large value
        matrix_last = [[0] * (column_count + 2) for _ in range(row_count + 1)]
        virtually_inf = row_count * column_count + 1
        for i in range(len(matrix_last)):
            matrix_last[i][0] = matrix_last[i][-1] = virtually_inf
        for j in range(len(matrix_last[0])):
            matrix_last[0][j] = virtually_inf

        # allowed movement directions
        deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

        # setup a priority queue for bfs
        # Days are negated to make the standard python min-heap into a max-heap
        prio_queue: list[tuple[int, int, int]] = []
        for j in range(1, column_count + 1):
            prio_queue.append((-matrix[1][j], 1, j))
        heapq.heapify(prio_queue)
        while prio_queue:
            _negated_day, i, j = heapq.heappop(prio_queue)
            day = -_negated_day
            # if this cell has previously been visited on a larger day, skip
            if day <= matrix_last[i][j]:
                continue
            # if other side has been reached, last day has been found
            if i == row_count:
                return day
            # update last day this cell can be reached
            matrix_last[i][j] = day
            # visit neighbors
            for d_i, d_j in deltas:
                new_i = i + d_i
                new_j = j + d_j
                # udpate last day to reach neighbor, depeding on day it is flooded
                new_day = min(day, matrix[new_i][new_j])
                if new_day <= matrix_last[new_i][new_j]:
                    # if neighbor has already been reached at a later day, do not bfs
                    continue
                # else push to queue
                heapq.heappush(prio_queue, (-new_day, new_i, new_j))

        # with correct input, should not be reached
        raise ValueError()
