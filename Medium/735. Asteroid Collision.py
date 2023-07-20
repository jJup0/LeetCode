class Solution:
    """
    We are given an array asteroids of integers representing asteroids in a row.

    For each asteroid, the absolute value represents its size, and the sign represents
    its direction (positive meaning right, negative meaning left). Each asteroid moves at
    the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids meet, the
    smaller one will explode. If both are the same size, both will explode. Two asteroids
    moving in the same direction will never meet.

    Constraints:
    - 2 <= asteroids.length <= 10^4
    - -1000 <= asteroids[i] <= 1000
    - asteroids[i] != 0
    """

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """Keep a stack of remaining asteroids and simulate crashes.
        O(n) / O(n)     time / space complexity
        """
        # stack of asteroids remaining after collisions
        remaining: list[int] = []

        for curr_asteroid in asteroids:
            # asteroids going right have nothing to collide with yet
            if curr_asteroid > 0:
                remaining.append(curr_asteroid)
                continue

            # asteroid is negative, i.e. travelling left
            curr_asteroid_size = -curr_asteroid
            while True:
                if not remaining or remaining[-1] < 0:
                    # all asteroids remaing are moving left, append to remaining
                    remaining.append(curr_asteroid)
                    break

                # last asteroid on the stack is moving right, so we will have a collision
                prev_asteroid_size = remaining[-1]
                if curr_asteroid_size > prev_asteroid_size:
                    # if the current asteroid is bigger, destory the last one on the stack
                    remaining.pop()
                elif curr_asteroid_size == prev_asteroid_size:
                    # if they are the same size destroy both
                    # (destroy current asteroid by not appending it to stack)
                    remaining.pop()
                    break
                else:
                    # else: current asteroid is smaller, destroy it
                    break

        return remaining
