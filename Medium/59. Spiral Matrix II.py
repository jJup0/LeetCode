from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # initliaze matrix structure
        res = [[0]*n for _ in range(n)]

        # next value to fill into matrix
        val = 1

        # avoid x is unbound warning in pylance
        x = 0

        # generate the matrix in rings, matrix has ceil(n/2) rings
        for ring in range((n//2)+1):
            # start y at level of ring
            y = ring
            # generate top row going from (ring, ring) going until (n-1-ring, ring)
            for x in range(ring, n-ring):
                res[y][x] = val
                val += 1

            # generate right column keeping x-value from before,
            # going from (n-1-ring, ring+1) to (n-1-ring, n-1-ring)
            for y in range(y+1, n-ring):
                res[y][x] = val
                val += 1

            # generate bottom row keeping y-value from before
            # going from (n-1-ring-1,  n-1-ring) to (ring, n-1-ring)
            for x in range(x-1, ring-1, -1):
                res[y][x] = val
                val += 1

            # generate left column keeping x-value from before
            # going from (ring, n-1-ring-1) to (ring, ring-1)
            for y in range(y-1, ring, -1):
                res[y][x] = val
                val += 1
        return res
