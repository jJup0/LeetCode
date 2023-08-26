class Solution:
    """
    You are given an array of n pairs pairs where pairs[i] = [left_i, right_i]
    and left_i < right_i.

    A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs
    can be formed in this fashion.

    Return the length longest chain which can be formed.

    You do not need to use up all the given intervals. You can select pairs
    n any order.

    Constraints:
    - n == pairs.length
    - 1 <= n <= 1000
    - -1000 <= lefti < righti <= 1000
    """

    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        Greedliy add pair with lowest `right` compatible with the chain so far.
        O(n * log(n)) / O(n)    time / space complexity
        """
        pairs.sort(key=lambda p: p[1])
        res = 0
        prev_right = -1001
        for left, right in pairs:
            if left > prev_right:
                res += 1
                prev_right = right
        return res
