class Solution:
    """
    You are given a list of bombs. The range of a bomb is defined as the area where its
    effect can be felt. This area is in the shape of a circle with the center as the
    location of the bomb.

    The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] =
    [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location
    of the ith bomb, whereas ri denotes the radius of its range.

    You may choose to detonate a single bomb. When a bomb is detonated, it will
    detonate all bombs that lie in its range. These bombs will further detonate
    the bombs that lie in their ranges.

    Given the list of bombs, return the maximum number of bombs that can be
    detonated if you are allowed to detonate only one bomb.


    Constraints:
        1 <= bombs.length <= 100
        bombs[i].length == 3
        1 <= xi, yi, ri <= 10^5
    """

    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        """O(n^2) / O(n)    time / space complexity"""
        n = len(bombs)
        overlaps_with: list[list[int]] = [[] for _ in range(n)]
        # find overlaps between bombs
        for i, (x1, y1, r1) in enumerate(bombs):
            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]

                dx = x2 - x1
                dy = y2 - y1
                dist_sqr = dx * dx + dy * dy

                if dist_sqr <= r1 * r1:
                    overlaps_with[i].append(j)
                if dist_sqr <= r2 * r2:
                    overlaps_with[j].append(i)

        def dfs(i: int):
            nonlocal curr_visited
            curr_visited.add(i)
            for neighbor in overlaps_with[i]:
                if neighbor not in curr_visited:
                    dfs(neighbor)

        # bombs to visit
        total_visited: set[int] = set()
        res = 0
        # dfs from each bomb, update result depending on how many bombs are visited
        for i in range(n):
            # visited bomb will already have dfs-ed
            if i in total_visited:
                continue
            curr_visited: set[int] = set()
            dfs(i)
            res = max(res, len(curr_visited))
            total_visited.update(curr_visited)
        return res
