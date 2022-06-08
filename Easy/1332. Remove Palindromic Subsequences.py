class Solution:
    """
    You are given a string s consisting only of letters 'a' and 'b'.
    In a single step you can remove one palindromic subsequence from s.
    Return the minimum number of steps to make the given string empty.
    A string is a subsequence of a given string if it is generated by deleting some
    characters of a given string without changing its order. Note that a subsequence
    does not necessarily need to be contiguous.
    A string is called palindrome if is one that reads the same backward as well as forward.
    Constraints:
        1 <= s.length <= 1000
        s[i] is either 'a' or 'b'.
    """

    def removePalindromeSub(self, s: str) -> int:
        # check if string is palindrome
        for i in range(len(s) // 2 + 1):
            if s[i] != s[-i-1]:
                # else there is at least one 'a' and one 'b'
                # all 'a's can be removed in one step and same for all 'b's
                return 2
        else:
            # if string is palidrome then return 1
            return 1
