class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        seen = [False] * len(arr)
        prev_group_idx = -1
        res = 0
        while prev_group_idx < len(arr) - 1:
            prev_group_idx = self._find_next_group(prev_group_idx, arr, seen)
            res += 1
        return res

    def _find_next_group(
        self, prev_group_idx: int, arr: list[int], seen: list[bool]
    ) -> int:
        """Finds the ending index of the next group.

        Args:
            prev_group_idx (int): Ending index of the previous group.
            arr (list[int]): Array to partition into groups.
            seen (list[bool]): Values which have been seen.

        Returns:
            int: Ending index of group starting at index `prev_group_idx + 1`.
        """
        search_start = prev_group_idx + 1
        next_val = search_start
        search = True
        idx = -1  # bind for type checker
        while search and next_val < len(arr):
            search = False
            idx = arr.index(next_val, search_start)
            for i in range(search_start, idx + 1):
                seen[arr[i]] = True
            for i in range(search_start, idx + 1):
                if not seen[i]:
                    search_start = idx
                    next_val = i
                    search = True
                    break
        return idx
