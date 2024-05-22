"""
Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        O(2^n * n) / O(2^n * n)     time / space complexity
        """

        # appends palindrome partitions to res
        def dfs(i: int, current_partition: list[str]):
            nonlocal palindrome_partitions, len_s, is_palindrome_memo
            # if end of string reached, add current partition
            if i == len_s:
                palindrome_partitions.append(current_partition.copy())
                return

            for j in range(i + 1, len_s + 1):
                # check all substrings s[i:j]
                substring = s[i:j]

                # unique value representing s[i:j]
                substring_id = i * len_s + j

                # use memoization for checking if subtring is a palindrome
                if substring_id not in is_palindrome_memo:
                    is_palindrome_memo[substring_id] = substring == substring[::-1]

                # if the substring is a palindrome, continue dfs
                if is_palindrome_memo[substring_id]:
                    # append substring, and pop after dfs
                    current_partition.append(substring)
                    dfs(j, current_partition)
                    current_partition.pop()

        # result variable
        palindrome_partitions: list[list[str]] = []

        len_s = len(s)

        # memoization for substring palindromes
        is_palindrome_memo: dict[int, bool] = {}

        dfs(0, [])
        return palindrome_partitions
