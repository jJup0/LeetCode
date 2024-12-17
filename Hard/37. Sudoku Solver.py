"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3
   sub-boxes of the grid.
The'.' character indicates empty cells.
Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or'.'.
- It is guaranteed that the input board has only one solution.
"""

from collections import Counter

BOX_LENGTH = 3
SIDE_LENGTH = BOX_LENGTH * BOX_LENGTH


class Solution:
    use_hidden_singles_strategy = True

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        n := side length of sudoku grid = 9
        """
        self.board = board
        self.remaining_count = sum(row.count(".") for row in board)
        self.solve_call_count_debug = 0
        self.hidden_singles_call_count_debug: Counter[int] = Counter()
        self.min_poss_debug: Counter[int] = Counter()
        self.solvable = self._solve(self._construct_allowed_nums(board))

    def _construct_allowed_nums(self, board: list[list[str]]) -> list[int]:
        """
        Complexity:
            Time: O(n^3)
            Space: O(n^2)
        """
        allowed_nums = [((1 << SIDE_LENGTH) - 1) << 1] * SIDE_LENGTH * SIDE_LENGTH
        for row_nr, row in enumerate(board):
            for colr_nr, val in enumerate(row):
                if val != ".":
                    self._set_num(row_nr, colr_nr, int(val), allowed_nums)
        return allowed_nums

    def _solve(self, allowed_nums: list[int]) -> bool:
        """
        Complexity:
            Time: O(n^O(n^2))
            Space: (n^2)
        """
        self.solve_call_count_debug += 1
        if self.remaining_count == 0:
            return True
        min_poss = SIDE_LENGTH
        min_row = min_col = -1
        for row_col, bm in enumerate(allowed_nums):
            bc = bm.bit_count()
            if bc > 0 and bc < min_poss:
                min_poss = bc
                min_row, min_col = divmod(row_col, SIDE_LENGTH)

        possible_digits = None
        if min_poss > 1 and self.use_hidden_singles_strategy:
            poss2, minrow2, mincol2, digit = self._find_hidden_single(allowed_nums)
            if poss2 == 1:
                min_row = minrow2
                min_col = mincol2
                possible_digits = [digit]

        self.min_poss_debug[min_poss] += 1
        self.remaining_count -= 1
        if possible_digits is None:
            possible_digits = self._get_possible_digits(min_row, min_col, allowed_nums)
        for digit in possible_digits:
            allowed_nums_copy = allowed_nums[:]
            self._set_num(min_row, min_col, digit, allowed_nums_copy)
            if self._is_possible_to_solve(allowed_nums_copy) and self._solve(
                allowed_nums_copy
            ):
                return True
            self.board[min_row][min_col] = "."
        self.remaining_count += 1
        return False

    def _find_hidden_single(self, allowed_nums: list[int]):
        """Turns out not to reduce the amount of calls to _solve() by much."""
        min_poss = SIDE_LENGTH
        min_row = min_col = min_digit = -1

        by_rows = [
            [row_nr * SIDE_LENGTH + col_nr for col_nr in range(SIDE_LENGTH)]
            for row_nr in range(SIDE_LENGTH)
        ]
        by_cols = [
            [row_nr * SIDE_LENGTH + col_nr for row_nr in range(SIDE_LENGTH)]
            for col_nr in range(SIDE_LENGTH)
        ]
        by_3x3 = [
            [r * SIDE_LENGTH + c for r, c in self._get_cells_in_square(row_nr, col_nr)]
            for row_nr in range(0, SIDE_LENGTH, BOX_LENGTH)
            for col_nr in range(0, SIDE_LENGTH, BOX_LENGTH)
        ]

        for division in [by_rows, by_cols, by_3x3]:
            for group in division:
                counts = [0] * (SIDE_LENGTH + 1)
                last_occ = [(-1, -1)] * (SIDE_LENGTH + 1)
                for cell_id in group:
                    row_nr, col_nr = divmod(cell_id, SIDE_LENGTH)
                    for digit in self._get_possible_digits(
                        row_nr, col_nr, allowed_nums
                    ):
                        counts[digit] += 1
                        last_occ[digit] = (row_nr, col_nr)

                for digit, occs in enumerate(counts):
                    if occs > 0 and occs < min_poss:
                        min_row, min_col = last_occ[digit]
                        min_poss = occs
                        min_digit = digit

        self.hidden_singles_call_count_debug[min_poss] += 1
        return min_poss, min_row, min_col, min_digit

    def _set_num(self, row: int, col: int, num: int, allowed_nums: list[int]):
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        # unset bit for value in allowed_nums for row, column and square
        bit_mask = ((1 << (SIDE_LENGTH + 1)) - 1) ^ (1 << num)
        for _col in range(SIDE_LENGTH):
            allowed_nums[row * SIDE_LENGTH + _col] &= bit_mask
        for _row in range(SIDE_LENGTH):
            allowed_nums[_row * SIDE_LENGTH + col] &= bit_mask
        for _row, _col in self._get_cells_in_square(row, col):
            allowed_nums[_row * SIDE_LENGTH + _col] &= bit_mask
        allowed_nums[row * SIDE_LENGTH + col] = 0

        self.board[row][col] = str(num)

    def _get_cells_in_square(self, row: int, col: int):
        top = (row // BOX_LENGTH) * BOX_LENGTH
        left = (col // BOX_LENGTH) * BOX_LENGTH
        return [
            (r, c)
            for r in range(top, top + BOX_LENGTH)
            for c in range(left, left + BOX_LENGTH)
        ]

    def _is_possible_to_solve(self, allowed_nums: list[int]) -> bool:
        """
        Complexity:
            Time: O(n^2)
            Space: O(1)
        """
        for row_nr, row in enumerate(self.board):
            for col_nr, val in enumerate(row):
                if val == "." and allowed_nums[row_nr * SIDE_LENGTH + col_nr] == 0:
                    return False
        return True

    def _get_possible_digits(
        self, row: int, col: int, possibles: list[int]
    ) -> list[int]:
        bm = possibles[row * 9 + col]
        return [i for i in range(1, SIDE_LENGTH) if bm & (1 << i)]


def isValidSudoku(board: list[list[str]]) -> bool:
    rows: list[set[str]] = [set() for _ in range(9)]
    cols: list[set[str]] = [set() for _ in range(9)]
    subboxes: list[set[str]] = [set() for _ in range(9)]
    for y, rowlist in enumerate(board):
        for x, entry in enumerate(rowlist):
            if entry != ".":
                subbox_idx = (y // 3) * 3 + x // 3

                if (
                    entry in rows[y]
                    or entry in (cols[x])
                    or entry in (subboxes[subbox_idx])
                ):
                    return False
                rows[y].add(entry)
                cols[x].add(entry)
                subboxes[subbox_idx].add(entry)
    return True


import copy
import random


def find_hard_boards():
    s = Solution()
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    removes_to_solve_count: list[list[int]] = [
        [] for _ in range(SIDE_LENGTH * SIDE_LENGTH)
    ]
    idxs = [(i, j) for i in range(SIDE_LENGTH) for j in range(SIDE_LENGTH)]
    for remove_count in range(60, SIDE_LENGTH * SIDE_LENGTH):
        for _ in range(50):
            bc1 = copy.deepcopy(board)
            random.shuffle(idxs)
            for i, j in idxs[:remove_count]:
                bc1[i][j] = "."

            num_occs = Counter(val for row in bc1 for val in row)
            missing_count = 0
            for i in range(1, SIDE_LENGTH + 1):
                missing_count += num_occs[str(i)] == 0
            if missing_count > 1:
                # two different ways of solving board
                continue

            bc2 = copy.deepcopy(bc1)
            s.use_hidden_singles_strategy = True
            s.solveSudoku(bc1)
            s_count1 = s.solve_call_count_debug
            removes_to_solve_count[remove_count].append(s_count1)
            # bc3 = copy.deepcopy(bc1)
            # s.use_hidden_singles_strategy = False
            # s.solveSudoku(bc3)
            # s_count2 = s.solve_call_count_debug

            # if s.solve_count > 1_000_000:
            if s.solve_call_count_debug > 10_000:
                print(f"hard board, {s.solve_call_count_debug}")
                print(bc2)
            assert isValidSudoku(bc1)
            # print(remove_count, s.solve_count)
        print(
            f"{remove_count}, avg={sum(removes_to_solve_count[remove_count])/len(removes_to_solve_count[remove_count])}"
        )


s = Solution()
find_hard_boards()
