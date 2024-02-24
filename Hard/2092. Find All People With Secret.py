"""
You are given an integer n indicating there are n people numbered from 0 to n -
1. You are also given a 0-indexed 2D integer array meetings where meetings[i] =
[x_i, y_i, time_i] indicates that person x_i and person y_i have a meeting at
time_i. A person may attend multiple meetings at the same time. Finally, you
are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson
at time 0. This secret is then shared every time a meeting takes place with a
person that has the secret. More formally, for every meeting, if a person x_i
has the secret at time_i, then they will share the secret with person y_i, and
vice versa.

The secrets are shared instantaneously. That is, a person may receive the
secret and share it with people in other meetings within the same time
frame.

Return a list of all the people that have the secret after all the meetings
have taken place. You may return the answer in any order.

Constraints:
- 2 <= n <= 10^5
- 1 <= meetings.length <= 10^5
- meetings[i].length == 3
- 0 <= x_i, y_i <= n - 1
- x_i != y_i
- 1 <= time_i <= 10^5
- 1 <= firstPerson <= n - 1
"""


class UnionFind:
    """
    Space complexity dependant on unique parameters passed to union().
    """

    def __init__(self, knows_secret: list[bool]) -> None:
        """
        O(1) / O(1)   time / space complexity
        """
        self.parent: dict[int, int] = {}
        self.knows_secret = knows_secret

    def union(self, p1: int, p2: int) -> None:
        """
        O(1) amortized / O(1)   time / space complexity
        """
        # add to union find if not present
        if p1 not in self.parent:
            self.parent[p1] = p1
        if p2 not in self.parent:
            self.parent[p2] = p2

        # if one of the people know the secret, share it
        if self.knows_secret[p1]:
            self.knows_secret[self.find(p2)] = True
        elif self.knows_secret[p2]:
            self.knows_secret[self.find(p1)] = True

        # perform actual union, by setting parent of one person to other
        curr_child_parent = self.find(p1)
        curr_parent_parent = self.find(p2)
        self.parent[curr_child_parent] = curr_parent_parent

    def find(self, p: int) -> int:
        """
        O(1) amortized / O(1)   time / space complexity
        """
        if p != self.parent[p]:
            # find ancestor, and flatten along the way
            self.parent[p] = self.find(self.parent[p])

        if self.knows_secret[self.parent[p]]:
            # get secret from ancestor
            self.knows_secret[p] = True
        return self.parent[p]


class Solution:
    def findAllPeople(
        self, n: int, meetings: list[list[int]], first_person: int
    ) -> list[int]:
        """
        m := len(meetings)
        O(m * log(m)) / O(n)     time / space complexity
        """
        meetings_count = len(meetings)

        knows_secret = [False] * n
        # person 0 and `first_person` know the secret
        knows_secret[0] = knows_secret[first_person] = True

        # sort meetings by meetings time
        meetings.sort(key=lambda meeting: meeting[2])

        i = 0
        while i < meetings_count:
            # create union find datastructure for all members
            # partitipating in meetings at this exact time
            meeting_time = meetings[i][2]
            uf = UnionFind(knows_secret)
            while i < meetings_count and meetings[i][2] == meeting_time:
                a, b, _ = meetings[i]
                uf.union(a, b)
                i += 1

            # call find() on all current people to update `knows_secret`
            for person in uf.parent:
                uf.find(person)

        # return list of all people who have come to know the secret
        return [i for i, knows in enumerate(knows_secret) if knows]
