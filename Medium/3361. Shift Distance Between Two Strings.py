"""
You are given two strings s and t of the same length, and two integer arrays
nextCost and previousCost.

In one operation, you can pick any index i of s, and perform either one of the
following actions:
- Shift s[i] to the next letter in the alphabet. If s[i] =='z', you should
  replace it with'a'. This operation costs nextCost[j] where j is the index of s[i]
  in the alphabet.
- Shift s[i] to the previous letter in the alphabet. If s[i] =='a', you should
  replace it with'z'. This operation costs previousCost[j] where j is the index of
  s[i] in the alphabet.

The shift distance is the minimum total cost of operations required to
transform s into t.

Return the shift distance from s to t.

Constraints:
- 1 <= s.length == t.length <= 10^5
- s and t consist only of lowercase English letters.
- nextCost.length == previousCost.length == 26
- 0 <= nextCost[i], previousCost[i] <= 10^9
"""


class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: list[int], previousCost: list[int]
    ) -> int:
        """
        Brute force, check for each character if it is cheaper to
        increase or decrease. No prefix sums or memoization used.
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        ord_a = ord("a")
        ord_z = ord("z")
        res = 0
        for c1, c2 in zip(s, t):
            c2_ord = ord(c2)
            # get cost for increasing
            cost_next = 0
            c1_ord = ord(c1)
            while c1_ord != c2_ord:
                cost_next += nextCost[c1_ord - ord_a]
                if c1_ord == ord_z:
                    c1_ord = ord_a
                else:
                    c1_ord += 1

            # get cost for decreasing
            cost_prev = 0
            c1_ord = ord(c1)
            while c1_ord != c2_ord:
                cost_prev += previousCost[c1_ord - ord_a]
                if c1_ord == ord_a:
                    c1_ord = ord_z
                else:
                    c1_ord -= 1

            res += min(cost_next, cost_prev)
        return res
