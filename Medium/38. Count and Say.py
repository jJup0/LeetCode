class Solution:
    """
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
        countAndSay(1) = "1"
        countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which
        is then converted into a different digit string.

    To determine how you "say" a digit string, split it into the minimal number of substrings
    such that each substring contains exactly one unique digit. Then for each substring, say the
    number of digits, then say the digit. Finally, concatenate every said digit.

    For example, the saying and conversion for digit string "3322251":

    https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg

    Given a positive integer n, return the nth term of the count-and-say sequence.

    Constraints:
        1 <= n <= 30
    """

    def countAndSay(self, n: int) -> str:
        """
        Empirically for n <= 50 result grows exponentially with base of around 1.4.
        O(n * 1.4^n) / O(1.4^n)      time / space complexity
        """

        # base case of 1, with termination symbol
        res = ["1", "$"]

        # "recursively" say res n-1 times
        for _ in range(n-1):
            next_res = []
            # previous digit
            prev = res[0][0]
            # streak count of previous digit
            count = 0
            # basically iterate over ''.join(res)
            for c in (c for word in res for c in word):
                if prev == c:
                    count += 1
                else:
                    # if previous digit is not the same, append count and digit, and reset streak
                    next_res.append(str(count) + prev)
                    count = 1
                    prev = c

            # append termination signal
            next_res.append('$')
            # switch res and next_res for next iteration
            res = next_res

        res.pop()  # pop the termination signal
        return ''.join(res)     # return as a single string
