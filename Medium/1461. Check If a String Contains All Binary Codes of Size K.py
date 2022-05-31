class Solution:
    """
    Given a binary string s and an integer k, return true if every binary code
    of length k is a substring of s. Otherwise, return false.
    Constraints:
        1 <= s.length <= 5 * 10^5
        s[i] is either '0' or '1'.
        1 <= k <= 20
        """

    def hasAllCodes(self, s: str, k: int) -> bool:
        # check if k is larger, otherwise can not iterate
        if k > len(s):
            return False

        # total codes possible with length k
        total_codes = (1 << k)
        # seen "array" to track which codes have already been achieved
        seen = [False] * total_codes

        # value to add on to current value when a '1' is encountered
        add_bit = total_codes >> 1

        # the current value of the current substring in s
        curr = int(s[-k:], base=2)

        # set it to seen and set the count to 1
        seen[curr] = True
        seen_count = 1

        # iterate through s from end to start, ignoring last k characters as they have already been looked at
        for i in range(len(s) - k - 1, -1, -1):
            # virtually pop off the last digit from the previous substring of s
            curr >>= 1
            # if the current character is a '1', add to current value
            if s[i] == '1':
                curr += add_bit
            # if the current value has not been seen before
            if not seen[curr]:
                # increase seen count, and check if all have been seen
                seen_count += 1
                if seen_count == total_codes:
                    return True
                # set current value as seen
                seen[curr] = True

        # if not found in the iteration, return false
        return False
