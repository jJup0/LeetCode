class Solution:
    """
    Given a wooden stick of length n units. The stick is labelled from 0 to n. For
    example, a stick of length 6 is labelled as follows:
    https://assets.leetcode.com/uploads/2020/07/21/statement.jpg

    Given an integer array cuts where cuts[i] denotes a position you should
    perform a cut at.

    You should perform the cuts in order, you can change the order of the
    cuts as you wish.

    The cost of one cut is the length of the stick to be cut, the total cost is the
    sum of costs of all cuts. When you cut a stick, it will be split into two
    smaller sticks (i.e. the sum of their lengths is the length of the stick
    before the cut). Please refer to the first example for a better explanation.

    Return the minimum total cost of the cuts.

    Constraints:
        2 <= n <= 106^
        1 <= cuts.length <= min(n - 1, 100)
        1 <= cuts[i] <= n - 1
        All the integers in cuts array are distinct.
    """

    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts.sort()
        self.cuts = cuts
        self.dp: dict[int, int] = {}
        return self._min_cost(0, n, 0, len(cuts))

    def _min_cost(
        self, stick_start: int, stick_stop: int, cut_start: int, cut_stop: int
    ) -> int:
        """Uses stick slice and cuts slice to find minimum using dynamic programming.
        Time complexity could be improved with "Knuths Optimization".
        n := len(cuts) = cut_stop - cut_start
        O(n^3) / O(n^2)     time / space complexity.
        """
        len_cuts = cut_stop - cut_start
        len_stick = stick_stop - stick_start
        # if no more cuts left, then none need to be done, costs are 0
        if len_cuts == 0:
            return 0
        # if one cut left, have to make that cut, return len stick
        if len_cuts == 1:
            return len_stick

        # cuts_list_slice_hash = (cut_start, cut_start) would be unique and the obvious
        # choice, but it's slow and we can exploit the fact that cuts is never larger
        # than 100 for a hash speed up
        cuts_list_slice_hash = cut_start * 1000 + cut_stop

        # if previously calculated, return that value
        if cuts_list_slice_hash in self.dp:
            return self.dp[cuts_list_slice_hash]

        # otherwise calculate value as minimum result over results of choosing the ith cut
        res = 1_000_000_000
        for cut_idx in range(cut_start, cut_stop):
            stick_cut_at = self.cuts[cut_idx]
            temp_res = len_stick
            temp_res += self._min_cost(stick_start, stick_cut_at, cut_start, cut_idx)
            temp_res += self._min_cost(stick_cut_at, stick_stop, cut_idx + 1, cut_stop)
            res = min(res, temp_res)

        # memoize computed value
        self.dp[cuts_list_slice_hash] = res
        return res
