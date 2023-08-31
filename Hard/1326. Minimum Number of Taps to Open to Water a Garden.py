class Solution:
    """
    There is a one-dimensional garden on the x-axis. The garden starts at the
    point 0 and ends at the point n. (i.e The length of the garden is n).

    There are n + 1 taps located at points [0, 1, ..., n] in the garden.

    Given an integer n and an integer array ranges of length n + 1 where ranges[i]
    (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]]
    if it was open.

    Return the minimum number of taps that should be open to water the whole garden,
    if the garden cannot be watered return -1.

    Constraints:
    - 1 <= n <= 10^4
    - ranges.length == n + 1
    - 0 <= ranges[i] <= 100
    """

    def minTaps(self, n: int, ranges: list[int]) -> int:
        """
        Greedy approach, sprinklers sorted by earliest covered index.
        Question is severely unclear, not only do all indexes have to be covered
        but the space between them as well, that means that for n = 3, ranges = [1,0,0,1]
        this is what the garden looks like:
        ----x----   ----x----
            0   1   2   3
        Notice that the space between 1 and 2 is not covered so we have to return -1.

        O(n*log(n)) / O(n)  time / space complexity
        """
        # convert sprinklers into intervals that they cover
        # 0-sprinklers do not do anything, so remove them
        start_stops = sorted(
            ((max(0, i - r), i + r) for i, r in enumerate(ranges) if r > 0),
            key=lambda x: x[0] * 1000 - x[1],
        )

        # pseudo sprinkler to make sure all necessary sprinklers are activated
        start_stops.append((n, n))
        # last garden index that is covered by a selected sprinkler
        covered = 0
        # last garden index that can be covered by a previously encounted,
        # not yet selected sprinkler
        max_next_stop = -1
        # result variable
        taps_needed = 0
        for start, stop in start_stops:
            if start > covered:
                # current sprinkler covers a plant which is not yet covered by a
                # previous sprinkler, so use one
                if max_next_stop < covered or max_next_stop < start:
                    return -1
                # update covered index
                covered = max_next_stop
                # increment result variable
                taps_needed += 1
                if covered >= n:
                    # return if all indexes covered
                    return taps_needed
            if stop > max_next_stop:
                # update next maximum stop if further
                max_next_stop = stop

        return -1
