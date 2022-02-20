from collections import Counter
from itertools import chain


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.retVal = False

        def searchBoard(ci, cj, _cli):
            if ci < 0 or cj < 0 or ci >= m or cj >= n or self.retVal:
                return
            if board[ci][cj] == word[_cli]:
                temp, board[ci][cj] = board[ci][cj], '/'
                _cli += 1
                if _cli == len(word):
                    self.retVal = True
                    return
                any(searchBoard(ci+di, cj+dj, _cli) for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                board[ci][cj] = temp

        if Counter(word) - Counter(chain(*board)):
            return False
        for i, row in enumerate(board):
            for j, boardletter in enumerate(row):
                if word[0] == boardletter:
                    searchBoard(i, j, 0)
                    if self.retVal:
                        return True
        return False
