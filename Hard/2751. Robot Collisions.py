"""
There are n 1-indexed robots, each having a position on a line, health, and
movement direction.

You are given 0-indexed integer arrays positions, healths, and a string
directions ( directions[i] is either'L' for left or'R' for right). All integers
in positions are unique.

All robots start moving on the line simultaneously at the same speed in their
given directions. If two robots ever share the same position while moving, they
will collide.

If two robots collide, the robot with lower health is removed from the line,
and the health of the other robot decreasesby one. The surviving robot
continues in the same direction it was going. If both robots have the same
health, they are bothremoved from the line.

Your task is to determine the health of the robots that survive the collisions,
in the same order that the robots were given,i.e. final heath of robot 1 (if
survived), final health of robot 2 (if survived), and so on. If there are no
survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order
they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.

Constraints:
- 1 <= positions.length == healths.length == directions.length == n <= 10^5
- 1 <= positions[i], healths[i] <= 10^9
- directions[i] =='L' or directions[i] =='R'
- All values in positions are distinct
"""


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        """
        O(n * log(n)) / O(n)
        """
        LEFT, RIGHT = "LR"

        # initial bots sorted by position
        # bots[i][3] is the original bot position, needed to construct result array
        bots = sorted(zip(positions, healths, directions, range(len(positions))))

        # currently surviving bots, monotone stack where bots at the bottom of the
        # stack are moving left, and bots at the top of the stack are moving right
        # bot_stack[i] = (original_idx, health, direction)
        bot_stack: list[tuple[int, int, str]] = []

        for _pos, curr_health, curr_dir, curr_bot_og_idx in bots:
            if curr_dir == RIGHT or not bot_stack or bot_stack[-1][2] == LEFT:
                # no collision will happen with previous bots
                bot_stack.append((curr_bot_og_idx, curr_health, curr_dir))
                continue

            # collide bots if current bot is going left and last bot on the stack is going right
            curr_bot_survived = True
            while bot_stack and bot_stack[-1][2] == RIGHT:
                other_bot_og_idx, other_bot_health, other_bot_dir = bot_stack.pop()
                if curr_health > other_bot_health:
                    # reduce health of current bot and go again
                    curr_health -= 1
                else:
                    # bot on the stack is stronger
                    curr_bot_survived = False
                    if other_bot_health > curr_health:
                        bot_stack.append(
                            (other_bot_og_idx, other_bot_health - 1, other_bot_dir)
                        )
                    break

            if curr_bot_survived:
                bot_stack.append((curr_bot_og_idx, curr_health, curr_dir))

        bot_stack.sort()
        return [bot[1] for bot in bot_stack]


s = Solution()
print(
    s.survivedRobotsHealths(
        [3, 5, 2, 6],
        [10, 10, 15, 12],
        "RLRL",
    )
)
