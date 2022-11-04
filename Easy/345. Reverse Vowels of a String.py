class Solution:
    """
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
    more than once.

    Constraints:
        1 <= s.length <= 3 * 10^5
        s consist of printable ASCII characters.
    """

    def reverseVowels(self, s: str) -> str:
        """
        O(n) / O(n)     time / space complexity
        """
        # convert to char array to make mutible
        char_arr = list(s)
        vowels = frozenset("aeiouAEIOU")

        # get indexes of all vowels
        vowel_idxs = [i for i, c in enumerate(s) if c in vowels]

        # go through vowel indexes and swap with opposite index
        for i in range(len(vowel_idxs)//2):
            index = vowel_idxs[i]
            opp_index = vowel_idxs[-i-1]
            char_arr[index], char_arr[opp_index] = char_arr[opp_index], char_arr[index]

        # convert back to string
        return "".join(char_arr)

    def reverseVowels_v1(self, s: str) -> str:
        char_arr = list(s)
        vowels = frozenset("aeiouAEIOU")
        reversed_vowels = (c for c in reversed(s) if c in vowels)
        for i in range(len(char_arr)):
            if char_arr[i] in vowels:
                char_arr[i] = next(reversed_vowels)
        return "".join(char_arr)
