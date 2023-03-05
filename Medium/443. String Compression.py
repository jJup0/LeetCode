class Solution:
    """
    Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating characters in chars:
        If the group's length is 1, append the character to s.
        Otherwise, append the character followed by the group's length.

    The compressed string s should not be returned separately, but instead, be stored in the input
    character array chars. Note that group lengths that are 10 or longer will be split into
    multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.
    """

    def compress(self, chars: list[str]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """

        def overwite_compressed(streak: int, prev_char: str, repl_idx: int) -> int:
            """Uses current streak, current character and current replacement
            index to compress current char sequence in place into chars.
            Returns new replacement index.
            """
            if streak == 1:
                # if their was no sequence of identical characters, just overwrite that single
                # character at the current overwrite index
                chars[repl_idx] = prev_char
                repl_idx += 1
            else:
                # let python stringify the character+streak value and overwrite at the current
                # index
                repl_string = prev_char + str(streak)
                for c in repl_string:
                    chars[repl_idx] = c
                    repl_idx += 1

            return repl_idx

        # track previous character while iterating over char array
        prev_char = chars[0]
        # current streak of same character
        streak = 0
        # idx at which to overwrite in chars
        repl_idx = 0

        # add a termination symbol to the end of chars, makes the function easier to write
        # In case this breaks some resizing threshold, takes O(n) time and space (technically against ).
        for c in chars:
            if c == prev_char:
                # if the current character is the same as the previous one, just increment
                streak += 1
            else:
                # compress in place
                repl_idx = overwite_compressed(streak, prev_char, repl_idx)
                # reset previous character and streak
                prev_char = c
                streak = 1

        # compress last char sequence and return index up until which chars is the compressed string
        repl_idx = overwite_compressed(streak, prev_char, repl_idx)
        return repl_idx
