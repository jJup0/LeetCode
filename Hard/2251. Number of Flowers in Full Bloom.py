import bisect


class Solution:
    """
    You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi]
    means the ith flower will be in full bloom from starti to endi (inclusive).
    You are also given a 0-indexed integer array people of size n, where people[i]
    is the time that the ith person will arrive to see the flowers.

    Return an integer array answer of size n, where answer[i] is the number of
    flowers that are in full bloom when the ith person arrives.

    Constraints:
    - 1 <= flowers.length <= 5 * 10^4
    - flowers[i].length == 2
    - 1 <= starti <= endi <= 10^9
    - 1 <= people.length <= 5 * 10^4
    - 1 <= people[i] <= 10^9
    """

    def fullBloomFlowers(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:
        return self.fullBloomFlowers_original(flowers, people)

    def fullBloomFlowers_original(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:
        """
        Sort flowers and people and then iterate through people in order of
        the day that they visited.
        O(n * log(n) + m * log(m)) / O(n + m)   time / space complexity
        """
        # assign flowers an id (their original index in flowers) and sort by
        # starting day ...
        flowers.sort()
        flowers_by_start = flowers
        # ... and also by ending day
        flowers_by_end = sorted(flowers_by_start, key=lambda f: f[1])
        # sort people by the day that they are visiting, but include their
        # original index in order to construct result
        people_sorted = sorted(
            (day, person_idx) for person_idx, day in enumerate(people)
        )

        n = len(flowers)
        # set of flower indices which are "currently" in full bloom
        currently_blooming = 0
        # result list
        res = [-1] * len(people)
        # indices of next flower to add/remove to/from blooming set
        flowers_start_i = flowers_end_i = 0

        for day, person_idx in people_sorted:
            # add flowers that have started to bloom
            while flowers_start_i < n and flowers_by_start[flowers_start_i][0] <= day:
                currently_blooming += 1
                flowers_start_i += 1
            # remove flowers which are no longer blooming
            while flowers_end_i < n and flowers_by_end[flowers_end_i][1] < day:
                currently_blooming -= 1
                flowers_end_i += 1

            # store the bloom count for the person
            res[person_idx] = currently_blooming

        return res

    def fullBloom_stolen_short(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:
        """
        Stolen from someone elses solution.
        O(n * log(n) + m * log(n)) / O(n + m)   time / space complexity
        """
        start = sorted([start for start, _ in flowers])
        end = sorted([end for _, end in flowers])
        return [
            bisect.bisect_right(start, day) - bisect.bisect_left(end, day)
            for day in people
        ]
