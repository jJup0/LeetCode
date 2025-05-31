"""
You are given an n x n integer matrix board where the cells are labeled from 1
to n^2 in a Boustrophedon style starting from the bottom left of the board
(i.e. board[n - 1][0] ) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do
the following:
- Choose a destination square next with a label in the range
  [curr + 1, min(curr + 6, n^2)].
  - This choice simulates the result of a standard 6-sided die roll: i.e.,
    there are always at most 6 destinations, regardless of the size of the board.
- If next has a snake or ladder, you must move to the destination of that snake
  or ladder. Otherwise, you move to next.
- The game ends when you reach the square n^2.

A board square on row r and column c has a snake or ladder if board[r][c]!= -1.
The destination of that snake or ladder is board[r][c]. Squares 1 and n^2 are
not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the
destination to a snake or ladder is the start of another snake or ladder, you
do not follow the subsequent snake or ladder.
- For example, suppose the board is [[-1,4],[-1,3]], and on the first move,
  your destination square is 2. You follow the ladder to square 3, but do not
  follow the subsequent ladder to 4.

Return the least number of dice rolls required to reach the square n^2. If it
is not possible to reach the square, return -1.

Constraints:
- n == board.length == board[i].length
- 2 <= n <= 20
- board[i][j] is either -1 or in the range [1, n^2].
- The squares labeled 1 and n^2 are not the starting points of any snake or ladder.
"""


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        goal = len(board) * len(board)
        board_array = self._board_to_array(board)
        # bfs frontier
        frontier = [1]
        # visited cells
        visited = [False] * (goal + 1)
        for dice_roll_nr in range(1, goal):
            if not frontier:
                break
            new_frontier: list[int] = []
            for pos in frontier:
                # perform all possible dice rolls for all possible previous positions
                for new_pos in range(pos + 1, min(pos + 7, goal + 1)):
                    destination = board_array[new_pos]
                    if visited[destination]:
                        continue
                    # if square is not previouly visited, add it to the frontier
                    new_frontier.append(destination)
                    visited[destination] = True
                    if destination == goal:
                        return dice_roll_nr

            # else increase step count, and update frontier for next round of bfs
            frontier = new_frontier

        # if goal never reached, return -1
        return -1

    def _board_to_array(self, board: list[list[int]]):
        """
        Flatten the board into a one dimensional array which maps the original board to its values.
        Board values are 1-indexed, so pad start of array with a single value.
        Also replaces -1 entries with the index.
        """
        number_to_board_value = [0]
        for i, row in enumerate(reversed(board)):
            if i & 1:
                # odd rows are reversed
                number_to_board_value.extend(reversed(row))
            else:
                number_to_board_value.extend(row)
        # replace -1 entries
        for i, num in enumerate(number_to_board_value):
            if num == -1:
                number_to_board_value[i] = i
        return number_to_board_value


def test():
    sol = Solution()
    res = sol.snakesAndLadders(
        [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
    )
    assert res == 4, res


test()
