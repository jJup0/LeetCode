from typing import Counter, List


class Solution:
    """
    A string s is called good if there are no two different characters in s that have the same
    frequency.
    Given a string s, return the minimum number of characters you need to delete to make s good.
    The frequency of a character in a string is the number of times it appears in the string.
    For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
    Constraints:
        1 <= s.length <= 10^5
        s contains only lowercase English letters.
    """

    def minDeletions(self, s: str) -> int:
        # result variable
        res = 0

        # all counts for characters
        counts = sorted(count for _, count in Counter(s).items())

        # previous count
        prev = 0

        # ranges of occurance count values that are not yet occupied
        # use ranges instead of concrete count values, in case counts looks something like [1, 1000000000]
        not_taken: List[List[int]] = []
        for count in counts:
            # if count is same as previous, need to removed letter
            if count == prev:
                # if there are occurances, 'delete' character until only not_taken[-1][1] characters remain
                if not_taken:
                    # get interval from not taken stack
                    (start, end) = taken = not_taken[-1]

                    # 'delete' required characters
                    res += count - end

                    # reduce interval by one
                    taken[1] -= 1

                    # if size of interval is 0, delete it
                    if start == taken[1]:
                        not_taken.pop()
                else:
                    # if there are no vacant occurance counts, delete all occurances of character
                    res += count
            else:
                # if counts are unequal
                # if a non empty interval of occurances can be append to not taken, do so
                if count - 1 > prev:
                    not_taken.append([prev, count-1])
                # update prev
                prev = count

        return res
