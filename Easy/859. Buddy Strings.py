from collections import Counter


class Solution:
    """
    Given two strings s and goal, return true if you can swap two letters in s
    so the result is equal to goal, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) such
    that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

    Constraints:
    - 1 <= s.length, goal.length <= 2 * 10^4
    - s and goal consist of lowercase letters.
    """

    def buddyStrings(self, s: str, goal: str) -> bool:
        return self.buddyStrings_optimized(s, goal)

    def buddyStrings_original(self, s: str, goal: str) -> bool:
        """
        O(n) / O(n)     time / space
        """
        s1c = Counter(s)
        s2c = Counter(goal)

        # if they have different character counts, return false
        if s1c != s2c:
            return False

        # if they are equal, at least one character must appear twice, so that
        # character can be switched with itself at a different position
        if s == goal:
            return max(s1c.values()) > 1

        # amount of positions that are different
        diff_counter = 0
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                diff_counter += 1
                # if three or more characters are different, a single swap will not suffice
                if diff_counter == 3:
                    return False

        # diff_counter == 2, char1 and char2 are different and exist at positions
        # i1 and i2, in both s and goal
        return True

    def buddyStrings_optimized(self, a: str, b: str) -> bool:
        """
        For some reason much faster in the leetcode benchmark, probably
        due to length check, and not using collections.Counter.
        O(n) / O(n)     time / space complexity
        """
        # unequal length, not even infinite swaps could make them equal
        if len(a) != len(b):
            return False

        if a == b:
            # if the strings are equal at least one character must appear twice
            return len(set(a)) < len(a)

        # let i1 and i2 be the first two indexes where a and b differ
        # a_c1 := a[i1], a_c2 := a[i2], etc.
        a_c1 = a_c2 = b_c1 = b_c2 = ""

        # iterate through all pairs of letters
        for c_a, c_b in zip(a, b):
            # if they are unequal
            if c_a != c_b:
                if not a_c1:
                    # first occurance of unequal
                    a_c1, b_c1 = c_a, c_b
                elif not a_c2:
                    # second occurance of unequal
                    a_c2, b_c2 = c_a, c_b
                else:
                    # thrid occurance of unequal, single swap is
                    # not enough to make strings equal
                    return False

        # a[i1] == b[i2] and a[i2] == b[i1] in order for the
        # swap to make the strings equal
        return a_c1 == b_c2 and a_c2 == b_c1
