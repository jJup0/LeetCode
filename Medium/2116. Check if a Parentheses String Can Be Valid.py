"""
A parentheses string is a non-empty string consisting only of'(' and')'. It is
valid if any of the following conditions is true:
- It is ().
- It can be written as AB ( A concatenated with B ), where A and B are valid
  parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n.
locked is a binary string consisting only of'0' s and'1' s. For each index i of
locked,
- If locked[i] is'1', you cannot change s[i].
- But if locked[i] is'0', you can change s[i] to either'(' or')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

Constraints:
- n == s.length == locked.length
- 1 <= n <= 10^5
- s[i] is either'(' or')'.
- locked[i] is either'0' or'1'.
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        if len(s) & 1:
            return False

        # unclose parentheses
        open_parenth = 0
        # parentheses closed by a wildcard
        wildcard_closed = 0
        # unused wildcards
        wildcard_unused = 0
        for lock, parenthesis in zip(locked, s):
            if lock == "0":
                # parenthesis is unlocked, treat as wildcard
                if open_parenth > 0:
                    # greedily close parenthesis, but track that this was done by a wildcard
                    open_parenth -= 1
                    wildcard_closed += 1
                else:
                    wildcard_unused += 1

            # parentheses are locked
            elif parenthesis == "(":
                open_parenth += 1

            # parenthesis == ")"
            elif open_parenth > 0:
                # greedily close unclosed parenthesis
                open_parenth -= 1
            elif wildcard_closed > 0:
                # if wildcards have close previous parenthesis then free up this wildcard
                wildcard_closed -= 1
                wildcard_unused += 1
            elif wildcard_unused > 0:
                # if unused wildcards exist treat one as an open parenthesis
                wildcard_unused -= 1
            else:
                # else the closing parenthesis has no partner
                return False
        # return true iff there are no unclosed parentheses
        return open_parenth == 0


def test():
    s = Solution()

    res = s.canBeValid("((", "01")
    assert res is False

    res = s.canBeValid("(((())))", "00011111")
    assert res is True

    res = s.canBeValid(
        "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
        "100011110110011011010111100111011101111110000101001101001111",
    )
    assert res is False

    res = s.canBeValid(
        "())()))()(()(((())(()()))))((((()())(())",
        "1011101100010001001011000000110010100101",
    )
    assert res is True

    res = s.canBeValid(
        "()))(()(()()()()(((())())((()((())",
        "1100000000000010000100001000001101",
    )
    assert res is True

    res = s.canBeValid(
        "(((()))(()(()())))())))((()(()()())())()(()())(()()(())())())(()((())))()())))(())((((((())))()())())))((((()))(((((((())))())()))(())(())()))(()))((()((()(()(()()(())(()((((())(()))((())))(())))()(())((()((()()(((((()))())()()()))()))(((())))((((()(((()))))",
        "101111111111010111101110110011010101001111110010111101110100101000100100110000010111000011100111111011010010100100011100110001100011000111000010100010000001101100011110111100010000100101110111000101111101100101001100100111111110011100110011111100110101001000",
    )
    assert res is True


def parenth_to_wildcard_string(string: str, locks: str):
    return "".join(c if l == "1" else "*" for c, l in zip(string, locks))


test()
