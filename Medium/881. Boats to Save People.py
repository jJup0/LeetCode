class Solution:
    """
    You are given an array people where people[i] is the weight of the ith person,
    and an infinite number of boats where each boat can carry a maximum weight of
    limit. Each boat carries at most two people at the same time, provided the sum
    of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.

    Constraints:
        1 <= people.length <= 5 * 10^4
        1 <= people[i] <= limit <= 3 * 10^4
    """

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """Greedily match heaviest people with lightest people.
        O(n)/ O(n)      time / space complexity
        """
        people.sort()
        boats = 0
        # indices of lightest and heaviest person not yet on a boat
        lightest_person_idx = 0
        heaviest_person_idx = len(people) - 1
        while lightest_person_idx <= heaviest_person_idx:
            # if lightest person can fit with heaviest person,
            # then place them both in the same boat
            if people[heaviest_person_idx] + people[lightest_person_idx] <= limit:
                lightest_person_idx += 1
            # heaviest person always goes on the boat
            heaviest_person_idx -= 1
            boats += 1

        return boats
