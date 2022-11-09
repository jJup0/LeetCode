class Solution:
    """
    Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or
            vice-versa.
        To make the string good, you can choose two adjacent characters that make the string
            bad and remove them. You can keep doing this until the string becomes good.

    Return the string after making it good. The answer is guaranteed to be unique under the given
    constraints.

    Notice that an empty string is also good.

    Constraints:
        1 <= s.length <= 100
        s contains only lower and upper case English letters.
    """

    def makeGood(self, s: str) -> str:
        """
        O(n) / O(n)   time / space complexity
        """
        
        # ord() of previous character, init to any value outside ord("A") and ord("z")
        prev_ord = 0
        
        # character array after deleting pairs
        res_char_arr = []
        for c in s:
            curr_ord = ord(c)
            # since only lower and uppper case letters, just check for ord difference of 32
            if abs(curr_ord - prev_ord) == 32:
                # if upper/lower case pair, delete last charcter in new char array, and update
                # prev_ord to last undeleted character
                res_char_arr.pop()
                prev_ord = ord(res_char_arr[-1]) if res_char_arr else 0
            else:
                # else do not delete current character i.e. append to new char array
                res_char_arr.append(c)
                prev_ord = curr_ord

        # return string representation of final char array
        return ''.join(res_char_arr)
