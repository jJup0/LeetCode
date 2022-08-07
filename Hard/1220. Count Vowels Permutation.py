class Solution:
    """
    Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
    Since the answer may be too large, return it modulo 10^9 + 7.
    Constraints:
        1 <= n <= 2 * 10^4
    """

    def countVowelPermutation(self, n: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """

        # count for amount of words that can start with each vowel
        ls = [1, 1, 1, 1, 1]

        # prepend each vowel to collection of previous words follwing the rules n-1 times
        for _ in range(n-1):
            ls = [
                ls[1],
                ls[0] + ls[2],
                sum(ls) - ls[2],
                ls[2] + ls[4],
                ls[0],
            ]

        # return the sum of words for starting with letter
        return sum(ls) % 1_000_000_007

    def countVowelPermutation_legibleLetterDict(self, n: int) -> int:
        ls = {c: 1 for c in "aeiou"}
        for _ in range(n-1):
            newls = {
                'a': ls['e'],
                'e': ls['a'] + ls['i'],
                'i': sum(ls.values()) - ls['i'],
                'o': ls['i'] + ls['u'],
                'u': ls['a'],
            }
            ls = newls
            print(ls)

        return sum(ls.values()) % 1_000_000_007


S = Solution()
S.countVowelPermutation(10)
