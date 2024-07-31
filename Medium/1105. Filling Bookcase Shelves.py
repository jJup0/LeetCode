"""
You are given an array books where books[i] = [thickness_i, height_i] indicates
the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total
width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their
thickness is less than or equal to shelfWidth, then build another level of the
shelf of the bookcase so that the total height of the bookcase has increased by
the maximum height of the books we just put down. We repeat this process until
there are no more books to place.

Note that at each step of the above process, the order of the books we place is
the same order as the given sequence of books.
- For example, if we have an ordered list of 5 books, we might place the first
  and second book onto the first shelf, the third book on the second shelf, and the
  fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after
placing shelves in this manner.

Constraints:
- 1 <= books.length <= 1000
- 1 <= thickness_i <= shelfWidth <= 1000
- 1 <= height_i <= 1000
"""

INT_INF = 1_000_000_000


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelf_width: int) -> int:
        return self.minHeightShelves_2(books, shelf_width)

    def minHeightShelves_recursive(
        self, books: list[list[int]], shelf_width: int
    ) -> int:
        """
        O(2^n) / O(n)   time / space complexity
        """

        def helper(starting_book_i: int, starting_height: int) -> int:
            """
            Return the minimum height of the bookshelf, starting a new book row
            with the `starting_book_i`th book, at `starting_height` units.
            """
            nonlocal books, shelf_width, best_starting_heights
            # check if previous better result calculated, if yes, return inf
            if best_starting_heights[starting_book_i] <= starting_height:
                return INT_INF
            best_starting_heights[starting_book_i] = starting_height

            #
            width_remaining = shelf_width
            max_height = books[starting_book_i][1]

            res = INT_INF
            i = -1  # bind i (for static type checker)
            for i in range(starting_book_i, len(books)):
                width, height = books[i]
                if width > width_remaining:
                    return min(res, helper(i, starting_height + max_height))
                if height > max_height:
                    res = min(res, helper(i, starting_height + max_height))
                    max_height = height
                width_remaining -= width

            # row is full or books ran out
            if i == len(books) - 1:
                res = min(res, starting_height + max_height)

            return res

        best_starting_heights = [INT_INF] * len(books)
        return helper(0, 0)

    def minHeightShelves_2(self, books: list[list[int]], shelf_width: int) -> int:
        """
        O(n^2) / O(n)   time / space complexity
        """
        # dp[i] := the minimum height to place the first i-1 books
        dp = [0] + [INT_INF] * len(books)

        for i in range(len(books)):
            row_width = 0
            row_max_height = 0
            # start a new row with books[i] as the last book, keep taking books
            # from previous rows onto the current row and store the minimum height
            for j in range(i, -1, -1):
                width, height = books[j]
                row_width += width
                if row_width > shelf_width:
                    break
                row_max_height = max(row_max_height, height)
                dp[i + 1] = min(dp[i + 1], dp[j] + row_max_height)

        return dp[-1]
