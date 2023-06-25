class Solution:
    """
    You are installing a billboard and want it to have the largest height. The
    billboard will have two steel supports, one on each side. Each steel support
    must be an equal height.

    You are given a collection of rods that can be welded together. For example,
    if you have rods of lengths 1, 2, and 3, you can weld them together to make
    a support of length 6.

    Return the largest possible height of your billboard installation. If you
    cannot support the billboard, return 0.

    Constraints:
    - 1 <= rods.length <= 20
    - 1 <= rods[i] <= 1000
    - sum(rods[i]) <= 5000
    """

    def tallestBillboard(self, rods: list[int]) -> int:
        return self.tallestBillboard_original(rods)

    def tallestBillboard_original(self, rods: list[int]) -> int:
        """Iterate over entire search space.
        n := len(rods), m := sum(rods)
        O(n * m) / O(m)     time / space complexity
        """
        # balances[i] = maximum height of right pole, with the right pole being i units higher than the left
        #   note: could analogously interpreted from perspective of the left pole
        balances = {0: 0}
        for r in rods:
            for balance, length in tuple(balances.items()):
                balance_add_left = balance - r
                balance_add_right = balance + r

                balances[balance_add_left] = max(
                    balances.get(balance_add_left, 0), length
                )
                balances[balance_add_right] = max(
                    balances.get(balance_add_right, 0), length + r
                )

        # maximum height of poles when they have the exact same height
        return balances[0]

    def tallestBillboard_half_half(self, rods: list[int]) -> int:
        """
        Create uneven pole pairs of each half of rods, and then put them together,
        if they have the same height difference.
        E.g. rods = [1, 3, 2, 4]:
                                                            |o|      |o|
                                           |o|              |o|      |o|
                 |x|                       |o|              |o|      |x|
                 |x|      +        |o|     |o|      =       |o|      |x|
        |x|      |x|               |o|     |o|              |x|      |x|

        Rods are marked with 'x' and 'o' to visualize how they fit together.
        """

        def helper(rods: list[int]) -> dict[int, int]:
            balances = {0: 0}
            for r in rods:
                for balance, length in tuple(balances.items()):
                    sub_ = balance - r
                    add_ = balance + r

                    balances[sub_] = max(balances.get(sub_, 0), length)
                    balances[add_] = max(balances.get(add_, 0), length + r)
            return balances

        half_len = len(rods) // 2
        rodsl = helper(rods[:half_len])
        rodsr = helper(rods[half_len:])
        return max(
            (length + rodsr[diff] - diff)
            for diff, length in rodsl.items()
            if diff in rodsr
        )
