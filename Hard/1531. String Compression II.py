from functools import cache


class Solution:
    """
    Run-length encoding is a string compression method that works by replacing consecutive
    identical characters (repeated 2 or more times) with the concatenation of the character and the
    number marking the count of the characters (length of the run). For example, to compress the
    string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
    becomes "a2bc3".

    Notice that in this problem, we are not adding '1' after single characters.

    iven a string s and an integer k. You need to delete at most k characters from s such that the
    run-length encoded version of s has minimum length.

    Find the minimum length of the run-length encoded version of s after deleting at most k
    characters.

    Constraints:
        1 <= s.length <= 100
        0 <= k <= s.length
        s contains only lowercase English letters.
    """

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Use caching decorator as dp for compressing a string, with a last deleted character, the
        deletion "streak" and the deletions remaining. Not sure if big-O is tightest bound.
        O(n^2 * k) / O(n^2 * k)     time / space complexity
        """

        n = len(s)
        MAX_COST = n + 1

        # count the cost of compressing s[start_idx:], with the last removed character being last_c
        @cache
        def counter(start_idx, last_c, last_count, deletions_remaining) -> int:
            # too many deletions used up, return impossibly high cost
            if deletions_remaining == -1:
                return MAX_COST

            # if whole string iterated through, no letter to be removed, therefore cost is 0
            if start_idx == n:
                return 0

            if s[start_idx] == last_c:
                # Keep this char for compression, deletion is handled in else case. Currently there
                # is a streak of the same chars with length last_count, how much longer is the
                # compressed string if current char is not removed and optimal chars are removed in
                # the remaining string
                extra_length_for_no_delete = last_count == 1 or last_count == 9 or last_count == 99
                return extra_length_for_no_delete + counter(start_idx + 1, last_c, last_count + 1, deletions_remaining)
            else:
                # compare minimum length of sting if current char is kept vs deleted and return minimum
                keep_counter = 1 + counter(start_idx + 1, s[start_idx], 1, deletions_remaining)
                del_counter = counter(start_idx + 1, last_c, last_count, deletions_remaining - 1)
                return min(keep_counter, del_counter)

        return counter(0, "", 0, k)

    def getLengthOfOptimalCompression_ignores_merges(self, s: str, k: int) -> int:
        # does not consider inputs like s="aaaaaabaaaaa", k=1
        run_lengths = []

        prev = s[0]
        streak = 0
        for c in s:
            if prev == c:
                streak += 1
            else:
                run_lengths.append(streak)
                prev = c
                streak = 1
        run_lengths.append(streak)

        if run_lengths and run_lengths[0] == 100:
            return len(str(100-k)) + 1

        res = sum(len(str(code)) for code in run_lengths) + sum(1 for code in run_lengths if code > 1)

        # what decreases: deleting single character, deleting second character, deleting 10th character, deleting 100th character

        run_lengths.extend(tuple(1 for _ in run_lengths))
        run_lengths.extend(tuple(9 for code in run_lengths if code >= 10))
        run_lengths.sort(key=lambda x: x if x < 10 else x - 9)
        for run_length in run_lengths:
            to_subtract = 1 if run_length == 1 else run_length - 1 if run_length < 10 else run_length - 9
            if to_subtract > k:
                break
            k -= to_subtract
            res -= 1

        return res
