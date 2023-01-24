class Solution:
    """
    You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a
    Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and
    alternating direction each row.

    You start on square 1 of the board. In each move, starting from square curr, do the following:

    Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
    This choice simulates the result of a standard 6-sided die roll: i.e., there are always at
    most 6 destinations, regardless of the size of the board.
    If next has a snake or ladder, you must move to the destination of that snake or ladder.
    Otherwise, you move to next.
    The game ends when you reach the square n2.
    A board square on row r and column c has a snake or ladder if board[r][c] != -1. The
    destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or
    ladder.

    Note that you only take a snake or ladder at most once per move. If the destination to a snake
    or ladder is the start of another snake or ladder, you do not follow the subsequent snake or
    ladder.

    For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination
    square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
    Return the least number of moves required to reach the square n2. If it is not possible to
    reach the square, return -1.

    Constraints:
        n == board.length == board[i].length
        2 <= n <= 20
        grid[i][j] is either -1 or in the range [1, n^2].
        The squares labeled 1 and n2 do not have any ladders or snakes.
    """

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        goal = len(board) * len(board)

        # flatten the board into a one dimensional array which maps the original board to its values
        # board values are 1-indexed, so start with single element
        number_to_board_value = [0]
        for i, row in enumerate(reversed(board)):
            if i & 1:
                # odd rows are reversed
                number_to_board_value.extend(reversed(row))
            else:
                number_to_board_value.extend(row)
        # pad the end to redirect to goal in order to prevent the need for out of bounds checks
        number_to_board_value.extend((goal, goal, goal, goal, goal))

        # result variable
        steps_needed = 0

        # bfs frontier
        frontier = [1]

        # set of visited square numbers
        visited = set(frontier)

        while frontier:
            new_frontier = []
            for pos in frontier:
                # perform all possible dice rolls for all possible previous positions
                for new_pos in range(pos + 1, pos + 7):
                    destination = number_to_board_value[new_pos]
                    if destination == -1:
                        # if destination is not a snake or ladder, then new_pos is destination
                        destination = new_pos
                    if destination not in visited:
                        # if square is not previouly visited, add it to the frontier
                        new_frontier.append(destination)
                        visited.add(destination)
            # if the goal has been reached, return the number of steps needed
            if goal in frontier:
                return steps_needed

            # else increase step count, and update frontier for next round of bfs
            steps_needed += 1
            frontier = new_frontier

        # if goal never reached, return -1
        return -1
