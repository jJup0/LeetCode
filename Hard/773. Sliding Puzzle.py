"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty
square represented by 0. A move consists of choosing 0 and a 4-directionally
adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that
the state of the board is solved. If it is impossible for the state of the
board to be solved, return -1.

Constraints:
- board.length == 2
- board[i].length == 3
- 0 <= board[i][j] <= 5
- Each value board[i][j] is unique.
"""


class Solution:
    def slidingPuzzle(self, starting_board: list[list[int]]) -> int:
        """
        x := number of squares
        Complexity:
            Time: O(x!)
            Space: O(x!)
        """
        self.goal_hash = self._board_to_hash([[1, 2, 3], [4, 5, 0]])
        self.visited: set[int] = set()
        queue = [starting_board]
        steps = 0
        while queue:
            new_queue: list[list[list[int]]] = []
            for b in queue:
                board_hash = self._board_to_hash(b)
                if board_hash == self.goal_hash:
                    return steps
                if board_hash in self.visited:
                    continue
                self.visited.add(board_hash)
                new_queue.extend(self._get_moves_for_board(b))
            queue = new_queue
            steps += 1
        return -1

    deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))

    def _get_moves_for_board(self, board: list[list[int]]):
        if 0 in board[0]:
            zero_row = 0
            zero_col = board[0].index(0)
        else:
            zero_row = 1
            zero_col = board[1].index(0)

        for drow, dcol in self.deltas:
            new_row = zero_row + drow
            new_col = zero_col + dcol
            if not self._is_on_board(new_row, new_col):
                continue

            other_val = board[new_row][new_col]

            board_copy = [board[0][:], board[1][:]]
            board_copy[zero_row][zero_col] = other_val
            board_copy[new_row][new_col] = 0
            yield board_copy

    def _board_to_hash(self, board: list[list[int]]):
        """Hash of a board's state, guaranteed collision-free.
        Complexity:
            Time: O(x)
            Space: O(1)
        """
        multi = 1
        hash_val = 0
        for row in board:
            for val in row:
                hash_val += val * multi
                multi *= 6
        return hash_val

    def _is_on_board(self, row: int, col: int):
        return 0 <= row <= 1 and 0 <= col <= 2
