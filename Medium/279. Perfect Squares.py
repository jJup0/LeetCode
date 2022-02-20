from math import sqrt


class Solution:

    def numSquares(self, n: int) -> int:
        # top down idea stolen and optimized with reversed tuple and more importantly set

        def is_divided(num, count):
            if count == 1:
                return num in squaresSet

            count -= 1
            for square in squares:
                if is_divided(num-square, count):
                    return True
            return False

        squares = tuple(i*i for i in range(int(sqrt(n)), 0, -1))
        squaresSet = set(squares)       # for checking if value in squares

        for count in range(1, 5):       # Lagrange's four-square theorem states max is 4
            if is_divided(n, count):
                return count

    def numSquaresOwn(self, n: int) -> int:
        squares = tuple(i*i for i in range(1, int(sqrt(n)) + 1))

        starts = [0]
        for count in range(1, 5):  # bfs, Lagrange's four-square theorem states max is 4
            idx = 0
            newStarts = []
            # newStarts = [-1]*len(starts) * len(squares) || reserves too much memory I guess, not all is used
            for start in starts:
                # if start == -1:
                #     break
                for square in squares:
                    val = start + square

                    if val == n:
                        return count
                    if val > n:
                        break

                    newStarts.append(val)
                    # newStarts[idx] = val
                    # idx += 1
            starts = newStarts

    def numSquaresMathematical(self, n: int) -> int:
        def isSquare(n): return (int(sqrt(n)) ** 2) == n

        if isSquare(n):     # if perfect square then return 1
            return 1

        # Lagrange's four-square theorem, idk i copied
        while n % 4 == 0:   # faster: n & 3 == 0
            n >>= 2

        if n % 8 == 7:      # faster: n & 7 == 7
            return 4

        for i in range(1, int(sqrt(n)) + 1):   # try all combinations for 2
            if isSquare(n - (i * i)):
                return 2

        return 3        # if none work, result is 3
