class Solution:
    """
    You are given an encoded string s. To decode the string to a tape, the encoded
    string is read one character at a time and the following steps are taken:

    - If the character read is a letter, that letter is written onto the tape.
    - If the character read is a digit d, the entire current tape is repeatedly
      written d - 1 more times in total.

    Given an integer k, return the kth letter (1-indexed) in the decoded string.

    Constraints:
    - 2 <= s.length <= 100
    - s consists of lowercase English letters and digits 2 through 9.
    - s starts with a letter.
    - 1 <= k <= 10^9
    - It is guaranteed that k is less than or equal to the length of the decoded
      string.
    - The decoded string is guaranteed to have less than 263 letters.
    """

    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        O(n) / O(1)     time / space complexity
        """
        # "build" the string according to the rules, but only store the length
        build_str_length = i = 0
        for i, c in enumerate(s):
            build_str_length = (
                build_str_length * int(c) if c.isdigit() else build_str_length + 1
            )
            if k <= build_str_length:
                break

        # iterate through the string backwards starting at index i
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                # if c is a digit, undo the length multiplication
                # integer division guaranteed to not truncate
                build_str_length //= int(c)
                # calculate k modulo build_str_length, since the current string
                # was just repeated c times, the kth character from the completely
                # built string is the same as the (k%len_before_multiplying)-th
                # character in the string built up to index j
                k %= build_str_length
            else:
                # since k is 1-indexed, k == 0 if the (original-k)th character
                # is the last character in a sequence of alphabetical characters
                if k == build_str_length or k == 0:
                    return c
                # character is alphabetical, reduce decrement length
                build_str_length -= 1

        raise ValueError(f"{s=} and {k=} are invalid inputs")
