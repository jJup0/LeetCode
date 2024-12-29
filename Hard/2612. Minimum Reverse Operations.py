"""
You are given an integer n and an integer p representing an array arr of length
n where all elements are set to 0's, except position p which is set to 1. You
are also given an integer array banned containing restricted positions. Perform
the following operation on arr:
- Reverse a subarray with size k if the single 1 is not set to a position in banned.

Return an integer array answer with n results where the ith result isthe
minimum number of operations needed to bring the single 1 to position i in arr,
or -1 if it is impossible.

Constraints:
- 1 <= n <= 10^5
- 0 <= p <= n - 1
- 0 <= banned.length <= n - 1
- 0 <= banned[i] <= n - 1
- 1 <= k <= n
- banned[i]!= p
- all values in banned are unique
"""

from collections import deque

from sortedcontainers import SortedList


class Solution:
    def minReverseOperations(
        self, n: int, p: int, banned: list[int], k: int
    ) -> list[int]:
        """
        Adapted from https://leetcode.com/problems/minimum-reverse-operations/solutions/3368819/python3-bfs-sortedlist-keep-track-of-remaining-nodes.

        Use sorted lists for unexplored and non-banned indexes to heavily cut down on time complexity.
        For unexplored indexes split into a list of even and odd indexes,
        as when performing reversals the new possible indexes are always 2 apart.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        is_banned = [False] * n
        for b in banned:
            is_banned[b] = True

        remaining_even_idxs = SortedList()
        remaining_odd_idxs = SortedList()
        for i in range(n):
            if i != p and not is_banned[i]:
                if i & 1:
                    remaining_odd_idxs.add(i)
                else:
                    remaining_even_idxs.add(i)

        queue = [p]
        dist = [-1] * n
        dist[p] = 0
        for index_of_1 in queue:
            # find lowest and highest index that the 1 can be switched
            # to after subarray reversals
            lowest_subarr_start = max(index_of_1 - k + 1, 0)
            lo = self._index_after_reverse(lowest_subarr_start, index_of_1, k)
            subarr_start_highest = min(index_of_1 + k - 1, n - 1) - (k - 1)
            hi = self._index_after_reverse(subarr_start_highest, index_of_1, k)

            if lo & 1:
                remaining = remaining_odd_idxs
            else:
                remaining = remaining_even_idxs

            # switch to all legal positions, set distance and remove from `remaining`
            for neighbor in tuple(remaining.irange(lo, hi)):
                queue.append(neighbor)
                dist[neighbor] = dist[index_of_1] + 1
                remaining.remove(neighbor)

        return dist

    def _index_after_reverse(self, subarr_start_idx: int, pos_of_1: int, k: int):
        # pos_of_1_in_subarr = pos_of_1 - subarr_start_idx
        # new_one_pos_in_subarr = k - 1 - pos_of_1_in_subarr
        # return  subarr_start_idx + new_one_pos_in_subarr
        # simplifies to:
        return 2 * subarr_start_idx + k - 1 - pos_of_1


class Solution1Incomplete:
    """
    First attempt, correct intuition, but complex implementation and incomplete.
    """

    def minReverseOperations(
        self, n: int, p: int, banned: list[int], k: int
    ) -> list[int]:
        self.smallest_unchecked = 0
        self.largest_unchecked = n - 1
        is_banned = [False] * n
        for b in banned:
            is_banned[b] = True

        # self.idx_to_next_unexplored = self._init_remaining_list_mapping(n, is_banned)
        self.unexplored_set = set(i for i in range(n) if not is_banned[i])
        self.unexplored_sorted = SortedList(self.unexplored_set)
        return self._bfs(n, p, is_banned, k)

    def _bfs(self, n: int, p: int, is_banned: list[bool], k: int):
        front = deque([p])
        steps_needed = [-1] * n
        step_count = 0
        while front:
            for _ in range(len(front)):
                val = front.popleft()
                if steps_needed[val] != -1:
                    continue
                steps_needed[val] = step_count
                self.unexplored_set.remove(val)
                self.unexplored_sorted.remove(val)
                new_positions = self._get_flip_positions(
                    n, val, is_banned, k, steps_needed
                )
                # for new_pos in new_positions:
                #     steps_needed[new_pos] = step_count
                # self.update_unchecked(is_banned, steps_needed)
                front.extend(new_positions)
            step_count += 1
        # steps_needed[p] = 0
        return steps_needed

    def _get_flip_positions(
        self, n: int, pos: int, is_banned: list[bool], k: int, steps_needed: list[int]
    ):
        left_start = pos - k + 1
        if left_start < 0:
            left_start = 0
        right_end = pos
        if right_end > n - k + 1:
            right_end = n - k + 1

        first_pos_after_flip = 2 * left_start + k - 1 - pos
        last_post_after_flip = 2 * right_end + k - 1 - pos
        sorted_list_i_start: int = self.unexplored_sorted.bisect_left(
            first_pos_after_flip
        )
        new_idxs: list[int] = []
        for sorted_list_i in range(sorted_list_i_start, len(self.unexplored_sorted)):
            actual_index: int = self.unexplored_sorted[sorted_list_i]
            if actual_index > last_post_after_flip:
                break
            if actual_index & 1 != first_pos_after_flip & 1:
                continue
            new_idxs.append(actual_index)

        # # for subarr_start in range(left_start, right_end):
        # for pos_after_flip in range(starting_i, last_post_after_flip, 2):
        #     # one_pos_in_subarr = pos - subarr_start
        #     # new_one_pos_in_subarr = k - 1 - one_pos_in_subarr
        #     # pos_after_flip = subarr_start + new_one_pos_in_subarr

        #     # pos_after_flip = subarr_start + k - 1 - (pos - subarr_start)
        #     # pos_after_flip = 2 * subarr_start + k - 1 - pos
        #     if is_banned[pos_after_flip] or steps_needed[pos_after_flip] != -1:
        #         continue
        #     new_idxs.append(pos_after_flip)
        return new_idxs
