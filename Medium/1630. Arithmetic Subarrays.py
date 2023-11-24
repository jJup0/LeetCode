"""
A sequence of numbers is called arithmetic if it consists of at least two
elements, and the difference between every two consecutive elements is the
same. More formally, a sequence s is arithmetic if and only if
s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:
```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

The following sequence is not arithmetic:

```
1, 1, 2, 5, 7
```
You are given an array of n integers, nums, and two arrays of m integers
each, l and r, representing the m range queries, where the ith query is
the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the
subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to
form an arithmetic sequence, and false otherwise.

Constraints:
- n == nums.length
- m == l.length
- m == r.length
- 2 <= n <= 500
- 1 <= m <= 500
- 0 <= l[i] < r[i] < n
- -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def checkArithmeticSubarrays(
        self, nums: list[int], ls: list[int], rs: list[int]
    ) -> list[bool]:
        """
        m := Total length of all queried sub arrays
        l := Max length of all queried sub arrays
        O(m) / O(l)     time / space complexity
        """
        self.nums = nums
        ress: list[bool] = []

        for l, r in zip(ls, rs):
            if l == r:
                ress.append(True)
                continue
            ress.append(self._is_arith_o_n(l, r))

        return ress

    def _is_arith_simple(self, l: int, r: int) -> bool:
        """
        Sorts sub array and checks if it is an arithmetic sequence.
        O(n * log(n)) / O(n)    time / space complexity
        """
        sub_arr = sorted(self.nums[l : r + 1])
        diff = sub_arr[1] - sub_arr[0]
        prev = sub_arr[0] - diff
        for num in sub_arr:
            if num - prev != diff:
                return False
            prev = num
        return True

    def _is_arith_o_n(self, l: int, r: int) -> bool:
        """
        Uses set to determine if a sequence is arithmetic
        O(n) / O(n)     time / space complexity
        """
        sub_arr = self.nums[l : r + 1]
        length_decremented = len(sub_arr) - 1
        smallest = min(sub_arr)
        largest = max(sub_arr)

        if (largest - smallest) % length_decremented:
            # arithmetic sequence would required a step count in the rational numbers
            return False

        diff_step = (largest - smallest) // length_decremented
        if diff_step == 0:
            # special case, cannot use range(_, _, 0)! All numbers must be the same.
            return all(n == smallest for n in sub_arr)

        # check if all numbers in the expected sequence are contained
        sub_arr_set = frozenset(sub_arr)
        for num in range(smallest, largest + 1, diff_step):
            if num not in sub_arr_set:
                return False
        return True
