"""
In the video game Fallout 4, the quest"Road to Freedom" requires players to
reach a metal dial called the"Freedom Trail Ring" and use the dial to spell a
specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and
another string key that represents the keyword that needs to be spelled, return
the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the"12:00" direction.
You should spell all the characters in key one by one by rotating ring
clockwise or anticlockwise to make each character of the string key aligned at
the"12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:
1. You can rotate the ring clockwise or anticlockwise by one place, which
   counts as one step. The final purpose of the rotation is to align one of ring's
   characters at the"12:00" direction, where this character must equal key[i].
2. If the character key[i] has been aligned at the"12:00" direction, press the
   center button to spell, which also counts as one step. After the pressing, you
   could begin to spell the next character in the key (next stage). Otherwise, you
   have finished all the spelling.

Constraints:
- 1 <= ring.length, key.length <= 100
- ring and key consist of only lower case English letters.
- It is guaranteed that key could always be spelled by rotating ring.
"""


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        return self.findRotateSteps_character_map(ring, key)

    def findRotateSteps_character_map(self, ring: str, key: str) -> int:
        """
        O(len(ring) + len(key)) / O(len(key) * len(ring)^2)
        """
        # lookup table for characters and positions in ring
        char_positions: dict[str, list[int]] = {c: [] for c in key}
        for i, char in enumerate(ring):
            if char in char_positions:
                char_positions[char].append(i)

        len_ring = len(ring)
        # maximum possible result, use as pseudo infinity
        INT_MAX = (len_ring + 1) * len(key)

        # mapping from current positions on the ring to the minimum amount of steps it takes to get there
        ring_position_to_min_steps: dict[int, int] = {0: 0}
        for key_char in key:
            new_ring_position_to_min_steps: dict[int, int] = {}
            # iterate through all current positions
            for curr_ring_position, steps in ring_position_to_min_steps.items():
                # iterate through all positions of the current `key` character we want to get to
                for position_of_next_key in char_positions[key_char]:
                    steps_to_key_char = abs(curr_ring_position - position_of_next_key)
                    # reduce steps if using the cycle (going from last to first or the other way around) uses fewer steps
                    steps_to_key_char = min(
                        steps_to_key_char, len_ring - steps_to_key_char
                    )
                    # update minimum steps to get to new position
                    new_ring_position_to_min_steps[position_of_next_key] = min(
                        new_ring_position_to_min_steps.get(
                            position_of_next_key, INT_MAX
                        ),
                        steps + steps_to_key_char + 1,
                    )

            # update position to steps mapping for next iteration
            ring_position_to_min_steps = new_ring_position_to_min_steps

        # return minimum steps needed to get to all different ending positions
        return min(ring_position_to_min_steps.values())

    def findRotateSteps_naive(self, ring: str, key: str) -> int:
        """
        n := len(ring), m := len(key)
        O(n^2 * m^2) / O(n * m)   time / space complexity
        """
        len_ring = len(ring)
        INT_MAX = (len_ring + 1) * len(key)
        dp = [[INT_MAX] * len_ring for _ in range(len(key))]
        # queue[i] = (current index in key, current index in ring)
        queue: list[tuple[int, int]] = [(0, 0)]
        steps = 0
        while True:
            steps += 1
            new_queue: list[tuple[int, int]] = []
            for key_idx, ring_pos in queue:

                if steps >= dp[key_idx][ring_pos]:
                    continue
                dp[key_idx][ring_pos] = steps

                if ring[ring_pos] == key[key_idx]:
                    if key_idx == len(key) - 1:
                        return steps
                    new_queue.append((key_idx + 1, ring_pos))
                    continue

                new_queue.append((key_idx, (ring_pos + 1 + len_ring) % len_ring))
                new_queue.append((key_idx, (ring_pos - 1 + len_ring) % len_ring))

            queue = new_queue
