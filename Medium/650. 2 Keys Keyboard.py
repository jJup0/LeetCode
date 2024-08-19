"""
There is only one character'A' on the screen of a notepad. You can perform one
of two operations on this notepad for each step:
- Copy All: You can copy all the characters present on the screen (a partial
  copy is not allowed).
- Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the
character'A' exactly n times on the screen.

Constraints:
- 1 <= n <= 1000
"""


class Solution:
    def minSteps(self, n: int) -> int:
        return self.minSteps_linear(n)

    def minSteps_n_squared(self, n: int) -> int:
        """
        Naive exploration with dynamic programming.
        O(n^2) / O(n^2)     time / space complexity
        """
        if n == 1:
            return 0

        # clipboard_visited[i] = clipboard values already "seen" when at value i
        clipboard_visited: list[set[int]] = [set() for _ in range(n + 1)]
        # current bfs exploration front
        queue = [(1, 0)]
        # steps taken
        steps = 0
        for steps in range(1, n + 1):
            new_queue: list[tuple[int, int]] = []
            # iterate through queue
            for a_count, in_clipboard in queue:
                # if already visited, skip
                if in_clipboard in clipboard_visited[a_count]:
                    continue
                # note as visited
                clipboard_visited[a_count].add(in_clipboard)

                # copy operation, only perform if clipboard is unequal to current count
                if a_count != in_clipboard:
                    new_queue.append((a_count, a_count))

                # paste operation, add to bfs front if less than n
                a_count += in_clipboard
                if a_count > n:
                    # overshot goal, skip
                    continue
                if a_count == n:
                    # shortest operation count found!
                    return steps
                new_queue.append((a_count, in_clipboard))

            # replace queue
            queue = new_queue

        raise Exception()

    def minSteps_linear(self, n: int) -> int:
        """
        Only copy into clipboard if current A count divides n.
        This approach basically finds prime factors of n and builds n that way.
        O(n) / O(1)    time / space complexity
        """
        if n == 1:
            return 0
        num = 1
        curr_copy = 1

        res = 1
        while num < n:
            if n % num == 0 and num != curr_copy:
                curr_copy = num
            else:
                num += curr_copy
            res += 1

        return res
