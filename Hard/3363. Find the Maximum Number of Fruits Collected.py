"""
There is a game dungeon comprised of n x n rooms arranged in a grid.

You are given a 2D array fruits of size n x n, where fruits[i][j] represents
the number of fruits in the room (i, j). Three children will play in the game
dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and
(n - 1, 0).

The children will make exactly n - 1 moves according to the following rules to
reach the room (n - 1, n - 1):
- The child starting from (0, 0) must move from their current room (i, j) to
  one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room
  exists.
- The child starting from (0, n - 1) must move from their current room (i, j)
  to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target
  room exists.
- The child starting from (n - 1, 0) must move from their current room (i, j)
  to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target
  room exists.

When a child enters a room, they will collect all the fruits there. If two or
more children enter the same room, only one child will collect the fruits, and
the room will be emptied after they leave.

Return the maximum number of fruits the children can collect from the dungeon.

Constraints:
- 2 <= n == fruits.length == fruits[i].length <= 1000
- 0 <= fruits[i][j] <= 1000
"""


class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        """
        Important realisation which makes this a medium problem:
            1. Top left child can only traverse along the diagonal.
            2. Greedily make other two children follow path that maximizes
               fruit without interfering with top left child.
               The algorithm is also simple.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        # fruits for top left child
        diag_fruits = sum(fruits[i][i] for i in range(len(fruits)))

        # fruits for top right child
        top_right = self._max_fruits_top_right(fruits)

        # not the most efficient, but we can simulate the bottom left
        # child by transposing fruits, and calling the same algorithm
        # as for top right
        fruits_transpose = list(zip(*fruits))
        bottom_left = self._max_fruits_top_right(fruits_transpose)

        return diag_fruits + top_right + bottom_left

    def _max_fruits_top_right(self, fruits: list[list[int]]):
        """
        Find the path that collects the most fruits starting from the
        top right of `fruits` and ending at the bottom right of fruits,
        excluding the fruits found at the bottom right square.
        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        n = len(fruits)
        prev_row = [0] * n
        prev_row[-1] = fruits[0][-1]

        for row_nr in range(1, n - 1):
            new_cols = [0] * n

            # # leftmost column to consider if we still want to reach square n-1, n-1
            leftmost_column = max(row_nr + 1, n - row_nr - 1)
            for j in range(n - 1, leftmost_column - 1, -1):
                most_fruits = 0
                if j < n - 1:
                    # if previous cell to the right exists, include it in most fruits
                    most_fruits = prev_row[j + 1]
                most_fruits = max(most_fruits, prev_row[j])
                most_fruits = max(most_fruits, prev_row[j - 1])
                new_cols[j] = most_fruits + fruits[row_nr][j]

            prev_row = new_cols
        return prev_row[-1]
