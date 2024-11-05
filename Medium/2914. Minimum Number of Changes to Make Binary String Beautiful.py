"""
You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more
substrings such that:
- Each substring has an even length.
- Each substring contains only 1's or only 0's.

You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.

Constraints:
- 2 <= s.length <= 10^5
- s has an even length.
- s[i] is either'0' or'1'.
"""


class Solution:
    def minChanges(self, s: str) -> int:
        return self.min_changes_one_liner(s)

    def min_changes_one_liner(self, s: str) -> int:
        """
        Since we want to make all series of 0s and 1s even, it is enough
        to check that each even index has the same value as each odd index
        and make a flip if is not so. This way we guarantee even series
        length while making minimum flips.
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))

    def min_changes_intuitive(self, s: str) -> int:
        """
        Greedily make series of 0s and 1s even, handling special case of a single 0 or 1.
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        partitions = self._partition_s(s)

        res = 0
        i = 0
        for i, count in enumerate(partitions):
            if not count % 2:
                # count is already even, do nothing
                continue

            # count is odd, and since all previous series have been (made)
            # even, this can not be the last series
            assert i < len(partitions) - 1

            res += 1
            if partitions[i + 1] != 1 and i < len(partitions) - 2:
                # Special case, next series is only one bit long, and bits
                # follow it add current count plus additional bit to next
                # series. For the sake of parity `+= 1` would suffice, but
                # this makes it more explicit
                partitions[i + 2] += count + 1

            # flip next bit to current bit
            partitions[i + 1] -= 1
        return res

    def _partition_s(self, s: str):
        """
        Get the streaks of 0s and 1s in s as a list of integers.
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        partitions: list[int] = []
        curr = s[0]
        count = 0
        for c in s:
            if c == curr:
                count += 1
            else:
                partitions.append(count)
                count = 1
                curr = c
        partitions.append(count)
        return partitions
