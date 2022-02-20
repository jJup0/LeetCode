class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows, cols, subboxes = ([set()for _ in range(9)]for _ in range(3))
        for y, rowlist in enumerate(board):
            for x, entry in enumerate(rowlist):
                if entry != '.':
                    if entry in rows[y] or entry in (cols[x]) or entry in (subboxes[(y//3)*3 + x//3]):
                        return False
                    rows[y].add(entry)
                    cols[x].add(entry)
                    subboxes[(y//3)*3 + x//3].add(entry)
        return True
