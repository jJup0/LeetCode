# # Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight


class Solution:
    """
    Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

    Return the root of the Quad-Tree representing the grid.

    Notice that you can assign the value of a node to True or False when isLeaf is False, and both
    are accepted in the answer.

    A Quad-Tree is a tree data structure in which each internal node has exactly four children.
    Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
    isLeaf: True if the node is leaf node on the tree or False if the node has the four children.

    Constraints:
        n == grid.length == grid[i].length
        n == 2x where 0 <= x <= 6
    """

    def construct(self, grid: list[list[int]]) -> 'Node':
        def _construct(x1: int, y1: int, size: int) -> 'Node':
            """
            Constructs and returns QuadTree node given x- and y-start indexes (of grid) and the "square" size to consider.
            x1, y1, size determine a submatrix of grid.
            """
            # store first value of the current submatrix
            first_val = grid[y1][x1]

            for y in range(y1, y1 + size):
                for x in range(x1, x1 + size):
                    # iterate through all values of the submatrix, and if a single value is
                    # different to the first value, then the submatrix has to be split again into 4 submatrices
                    if grid[y][x] != first_val:
                        half_size = size // 2
                        top_left_child = _construct(x1, y1, half_size)
                        top_right_child = _construct(x1 + half_size, y1, half_size)
                        bottom_left_child = _construct(x1, y1 + half_size, half_size)
                        bottom_right_child = _construct(x1 + half_size, y1 + half_size, half_size)
                        return Node(1, False, top_left_child, top_right_child, bottom_left_child, bottom_right_child)

            # if every value in the current submatrix is the same, return a leaf node with
            # that value
            return Node(first_val, True, None, None, None, None)

        # return QuadTree node constructed by giving entire grid as input to _construct()
        return _construct(0, 0, len(grid))
