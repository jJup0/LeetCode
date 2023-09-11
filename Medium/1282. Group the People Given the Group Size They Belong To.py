from collections import defaultdict


class Solution:
    """
    There are n people that are split into some unknown number of groups. Each
    person is labeled with a unique ID from 0 to n - 1.

    You are given an integer array groupSizes, where groupSizes[i] is the size
    of the group that person i is in. For example, if groupSizes[1] = 3, then
    person 1 must be in a group of size 3.

    Return a list of groups such that each person i is in a group of size
    groupSizes[i].

    Each person should appear in exactly one group, and every person must be in
    a group. If there are multiple answers, return any of them. It is guaranteed
    that there will be at least one valid solution for the given input.

    Constraints:
    - groupSizes.length == n
    - 1 <= n <= 500
    - 1 <= groupSizes[i] <= n
    """

    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        # mapping from target group sizes to current members of an unfilled
        # group of that size
        size_to_curr_members: defaultdict[int, list[int]] = defaultdict(list)

        # iterate through members and add them to groups
        for i, size in enumerate(groupSizes):
            # get members so far that need group of size `size`
            curr_group = size_to_curr_members[size]
            # add current person to group
            curr_group.append(i)
            if len(curr_group) == size:
                # if the group has reached its target size, append it to the result
                # array, and reset in case there are multiple groups of size `size`
                res.append(curr_group)
                size_to_curr_members[size] = []

        return res
