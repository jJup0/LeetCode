from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        """
        BFS approach
        O(n * sqrt(n)) / O(n)   time / space complexity
        """
        squares = tuple(i*i for i in range(1, int(sqrt(n)) + 1))

        # list of all values reachable with sum of _count_ perfect-squares
        values_reached = set((0,))
        for count in range(1, 5):  # Lagrange's four-square theorem states max is 4
            # list of all values reachable with sum of _count_+1 perfect-squares
            next_values_reached = set()

            # iterate through all values reachable with _count_-1 perfect squares
            for val in values_reached:
                # get all reachable values from val by adding a perfect square
                for square in squares:
                    new_val = val + square

                    # if that square is the target, return
                    if new_val == n:
                        return count
                    # if it is bigger than break, because values in squares are ascending
                    if new_val > n:
                        break

                    # add to next batch of values
                    next_values_reached.add(new_val)

            values_reached = next_values_reached
        
        assert(False)

    def numSquaresStolen(self, n: int) -> int:
        # bfs but with top down approach and 1 less level to check

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
        
        assert(False)

    def numSquaresMathematical(self, n: int) -> int:
        """
        Mathematically optimal, Lagranges four square theorem applied
        """

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
