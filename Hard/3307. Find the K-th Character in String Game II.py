"""
Alice and Bob are playing a game. Initially, Alice has a string word ="a".

You are given a positive integer k. You are also given an integer array
operations, where operations[i] represents the type of the ith operation.

Now Bob will ask Alice to perform all operations in sequence:
- If operations[i] == 0, append a copy of word to itself.
- If operations[i] == 1, generate a new string by changing each character in
  word to its next character in the English alphabet, and append it to the original
  word. For example, performing the operation on"c" generates"cd" and performing
  the operation on"zb" generates"zbac".

Return the value of the kth character in word after performing all the operations.

Note that the character'z' can be changed to'a' in the second type of operation.

Constraints:
- 1 <= k <= 10^14
- 1 <= operations.length <= 100
- operations[i] is either 0 or 1.
- The input is generated such that word has at least k characters after all
  operations.
"""


class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        """
        The last index in operations needed to make a string with at least k
        characters is the order of magnitude of k (0-indexed) in base 2.

        Lets say the `k`th letter in the resulting string is the `x`th
        letter from the end. If the last operation is 0, then the `k`th
        letter is the same as the `x`th letter from the end of the string
        before the last operation. If the last operation is 1 then it is just 1
        greater (also account for wrap around).
        Keep applying this halving logic until we arrive at the first letter.

        Complexity:
            Time: O(log(k))
            Space: O(log(k))
        """
        self.operations = operations
        letter_idx = self._kth_character_helper(k) % 26
        return chr(ord("a") + letter_idx)

    def _kth_character_helper(self, k: int) -> int:
        """Recursively calculated kth letter by chopping away b"""
        if k == 1:
            return 0
        operation_idx = (k - 1).bit_length() - 1
        next_k = k - (1 << (operation_idx))
        return self._kth_character_helper(next_k) + (
            self.operations[operation_idx] == 1
        )

    def trivial(self, k: int, operations: list[int]):
        """Trivial implementation to test real implementation."""
        chars = ["a"]
        for op in operations:
            if len(chars) >= k:
                break
            chars.extend(chr(ord(c) + op) for c in chars[:])
        return chars[k - 1]


def test():
    import random

    sol = Solution()
    for i in range(1, 1000):
        operations = [random.randint(0, 1) for _ in range(10)]
        res = sol.kthCharacter(i, operations)
        real = sol.trivial(i, operations)
        assert res == real, f"{res=} {real=}"


test()
