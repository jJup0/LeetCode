class Solution:
    """
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.
    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        def next_char(string, idx):
            """Gets the next charater of a special encoded string.
            Parameters
            string : str
                String to get next character of
            idx : int
                End index (exclusive) from which to start "searching" from
            Returns
                A tuple with the next character, and the index with which to call the function the next time
            """

            idx -= 1
            # keep track of how many '#' were encountered so far
            backspaces = 0
            while idx > -1:
                c = string[idx]
                # if the char is a back space, add to count
                if c == '#':
                    backspaces += 1
                elif backspaces:
                    # else, if there are backspaces left to consume, do so
                    backspaces -= 1
                else:
                    # else return the character
                    return c, idx
                idx -= 1
            # function was either called with idx=0, or backspaces "deleted" all remaining characters
            return None, 0

        s_idx = len(S)
        t_idx = len(T)
        # compare strings in reverse, to make working with backspaces easier
        while s_idx or t_idx:
            s_c, s_idx = next_char(S, s_idx)
            t_c, t_idx = next_char(T, t_idx)
            # if next characters are different return false
            if s_c != t_c:
                return False
        # if all characters were the same, return true
        return True
