class Solution:
    """
    You have a pointer at index 0 in an array of size arrLen. At each step, you
    can move 1 position to the left, 1 position to the right in the array, or
    stay in the same place (The pointer should not be placed outside the array
    at any time).

    Given two integers steps and arrLen, return the number of ways such that your
    pointer is still at index 0 after exactly steps steps. Since the answer may be
    too large, return it modulo 10^9 + 7.

    Constraints:
    - 1 <= steps <= 500
    - 1 <= arrLen <= 10^6
    """

    def numWays(self, steps: int, arr_len: int) -> int:
        """
        O(steps * min(steps, arr_len)) / O(min(steps, arr_len))     time / space complexity
        """
        if arr_len == 1:
            # separately handling this edge case make main procedure simpler
            return 1

        MOD = 10**9 + 7

        # an arrLen > steps // 2 + 1 will have no effect on the result, as we
        # cannot step until the end of the array and back to 0 in time
        arr_len = min(steps // 2 + 1, arr_len)

        # ways[i] = ways to get to position i in the current amount of steps
        ways = [0] * arr_len
        # starting at position 0 -> there is one way to get to position 0 without moving
        ways[0] = 1
        # need a temporary array to add new ways for each iteration
        next_ways = ways.copy()

        for _ in range(steps):
            # first position has no left neighbor, so handle separately
            next_ways[1] = (next_ways[1] + ways[0]) % MOD
            # for each position with left and right neigbors, update the count
            for i in range(1, arr_len - 1):
                curr_way = ways[i]
                next_ways[i - 1] = (next_ways[i - 1] + curr_way) % MOD
                next_ways[i + 1] = (next_ways[i + 1] + curr_way) % MOD

            # last position has no right neighbor, so handle separately
            next_ways[-2] = (next_ways[-2] + ways[-1]) % MOD
            # update ways
            ways = next_ways.copy()

        return ways[0]
