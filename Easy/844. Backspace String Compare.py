class Solution:
    """
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.
    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        def doBackspace(string):
            retVal = []
            curDeletes = 0
            for c in reversed(string):
                if c == '#':
                    curDeletes += 1
                else:
                    if curDeletes:
                        curDeletes -= 1
                    else:
                        retVal.append(c)
            return retVal

        return doBackspace(S) == doBackspace(T)
