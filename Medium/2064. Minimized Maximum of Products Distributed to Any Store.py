"""
You are given an integer n indicating there are n specialty retail stores.
There are m product types of varying amounts, which are given as a 0-indexed
integer array quantities, where quantities[i] represents the number of products
of the ith product type.

You need to distribute all products to the retail stores following these rules:
- A store can only be given at most one product type but can be given any
  amount of it.
- After distribution, each store will have been given some number of products
  (possibly 0 ). Let x represent the maximum number of products given to any store.
  You want x to be as small as possible, i.e., you want to minimize the maximum
  number of products that are given to any store.

Return the minimum possible x.

Constraints:
- m == quantities.length
- 1 <= m <= n <= 10^5
- 1 <= quantities[i] <= 10^5
"""

import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        """
        Binary search for a quantity to place in each store.
        Complexity:
            Time: O(n * log(n))
            Space: O(1)
        """
        # lower and upper limit (inclusive) of the maximum amount
        # of products to distribute to each store
        per_store_min = max(1, sum(quantities) // n)
        per_store_max = max(quantities)
        # binary search for result
        while per_store_min < per_store_max:
            per_store = (per_store_min + per_store_max) // 2
            stores_needed = sum(math.ceil(q / per_store) for q in quantities)
            if stores_needed <= n:
                per_store_max = per_store
            else:
                per_store_min = per_store + 1
        return per_store_min
