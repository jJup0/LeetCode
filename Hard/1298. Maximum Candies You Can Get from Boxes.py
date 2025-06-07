"""
You have n boxes labeled from 0 to n - 1. You are given four arrays: status,
candies, keys, and containedBoxes where:
- status[i] is 1 if the ith box is open and 0 if the ith box is closed,
- candies[i] is the number of candies in the ith box,
- keys[i] is a list of the labels of the boxes you can open after opening the
  ith box.
- containedBoxes[i] is a list of the boxes you found inside the ith box.

You are given an integer array initialBoxes that contains the labels of the
boxes you initially have. You can take all the candies in any open box and you
can use the keys in it to open new boxes and you also can use the boxes you
find in it.

Return the maximum number of candies you can get following the rules above.

Constraints:
- n == status.length == candies.length == keys.length == containedBoxes.length
- 1 <= n <= 1000
- status[i] is either 0 or 1.
- 1 <= candies[i] <= 1000
- 0 <= keys[i].length <= n
- 0 <= keys[i][j] < n
- All values of keys[i] are unique.
- 0 <= containedBoxes[i].length <= n
- 0 <= containedBoxes[i][j] < n
- All values of containedBoxes[i] are unique.
- Each box is contained in one box at most.
- 0 <= initialBoxes.length <= n
- 0 <= initialBoxes[i] < n
"""


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        """
        DFS open boxes, keep a stack of unlocked boxes, set of locked
        boxes, and bit-array of boxes that can be unlocked.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # stack of boxes ready to open
        unlocked_boxes: list[int] = []
        # boolean map of boxes which we have, but no key
        box_owned_but_locked = [False] * len(status)
        for box in initialBoxes:
            if status[box]:
                unlocked_boxes.append(box)
            else:
                box_owned_but_locked[box] = True

        # result variable, total candies we can get
        candies_res = 0
        while unlocked_boxes:
            box = unlocked_boxes.pop()
            # take all candies
            candies_res += candies[box]
            # process all keys
            for key_for_box in keys[box]:
                status[key_for_box] = 1
                if box_owned_but_locked[key_for_box]:
                    # key is for a previously found box, unlock it
                    unlocked_boxes.append(key_for_box)
                    box_owned_but_locked[key_for_box] = False
            # process boxes contained in this box
            for contained_box in containedBoxes[box]:
                if status[contained_box] == 1:
                    # we have the key for this box, append to stack
                    unlocked_boxes.append(contained_box)
                else:
                    # we cannot open this box
                    box_owned_but_locked[contained_box] = True

        return candies_res


def test():
    import json
    from typing import Any

    sol = Solution()

    res = sol.maxCandies(
        [1, 0, 1, 0],
        [7, 5, 4, 100],
        [[], [], [1], []],
        [[1, 2], [3], [], []],
        [0],
    )
    assert res == 16
    args: list[Any] = []
    with open("big_input.txt") as f:
        for line in f:
            args.append(json.loads(line))
    res = sol.maxCandies(*args)
    assert res == 23185, res


test()
