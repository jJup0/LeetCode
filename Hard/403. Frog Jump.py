from functools import cache


class Solution:
    """
    A frog is crossing a river. The river is divided into some number of units,
    and at each unit, there may or may not exist a stone. The frog can jump on
    a stone, but it must not jump into the water.

    Given a list of stones' positions (in units) in sorted ascending order,
    determine if the frog can cross the river by landing on the last stone.
    Initially, the frog is on the first stone and assumes the first jump must
    be 1 unit.

    If the frog's last jump was k units, its next jump must be either k - 1, k,
    or k + 1 units. The frog can only jump in the forward direction.

    Constraints:
    - 2 <= stones.length <= 2000
    - 0 <= stones[i] <= 2^31 - 1
    - stones[0] == 0
    - stones is sorted in a strictly increasing order.
    """

    def canCross(self, stones: list[int]) -> bool:
        @cache
        def _can_cross(stone_idx: int, previous_jump: int):
            nonlocal stones, unit_to_stone_idx
            if stone_idx == len(stones) - 1:
                # final stone is reached, return true
                return True

            curr_pos = stones[stone_idx]
            # there are three jump ranges availible, but a jump needs to at least
            # have a distance of 1 to avoid backwards or on the same rock
            for jump_range in range(max(1, previous_jump - 1), previous_jump + 2):
                next_unit = curr_pos + jump_range
                if next_unit in unit_to_stone_idx:
                    # there is a rock availible to jump to
                    if _can_cross(unit_to_stone_idx[next_unit], jump_range):
                        # end can be reached with the current jump, return true
                        return True

            # end cannot be reached with any availible jumps, return false
            return False

        # mapping from a stones position to its index in `stones`
        unit_to_stone_idx = {unit: idx for idx, unit in enumerate(stones)}

        return _can_cross(0, 0)
