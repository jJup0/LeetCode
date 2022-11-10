class Solution:
    """
    You are given a string s consisting of lowercase English letters. A duplicate removal consists
    of choosing two adjacent and equal letters and removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It can be proven that
    the answer is unique.

    Constraints:
        1 <= s.length <= 10^5
        s consists of lowercase English letters.
    """

    def removeDuplicates(self, s: str) -> str:
        """
        O(n) / O(n)   time / space complexity
        """

        # previous character, init to any value outside 'a'-'z'
        prev_c = '$'

        # character stack after deleting adjacent duplicates
        res_char_stack = []
        for c in s:
            if c == prev_c:
                # if prev character same as current, delete previous character and update prev_c to
                # last undeleted character
                res_char_stack.pop()
                prev_c = res_char_stack[-1] if res_char_stack else '$'
            else:
                # else append current char to new char array
                res_char_stack.append(c)
                prev_c = c

        # return string representation of final char array
        return ''.join(res_char_stack)
