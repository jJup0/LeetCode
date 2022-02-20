class Solution:
    def solve(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])
        safePieces = {xy for y in range(n) for xy in ((0, y), (m-1, y))}.union({xy for x in range(1, m-1) for xy in ((x, 0), (x, n-1))})  # == all edge pieces

        while safePieces:
            y, x = safePieces.pop()
            if 0 <= y < m and 0 <= x < n and board[y][x] == 'O':
                board[y][x] = 'S'
                safePieces.update({(y, x-1), (y, x+1), (y-1, x), (y+1, x)})   # add all neighbouring pieces of a safe 'O' to safe set

        board[:] = [['O' if c == 'S' else 'X' for c in row] for row in board]
