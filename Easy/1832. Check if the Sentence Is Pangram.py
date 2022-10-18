class Solution:
    """
    A pangram is a sentence where every letter of the English alphabet appears at least once.
    Given a string sentence containing only lowercase English letters, return true if sentence is a
    pangram, or false otherwise.

    Constraints:
        1 <= sentence.length <= 1000
        sentence consists of lowercase English letters.
    """

    def checkIfPangram(self, sentence: str) -> bool:
        """
        Faster than one-liner for inputs like "abc ... xyzaaaaaaaaaaaaaa ..."
        O(n) / O(1)     time / space complexity
        """

        # create set for seen chars
        chars = set()

        # iterate through sentence and add to set, check if set has all letters
        for c in sentence:
            chars.add(c)
            if len(chars) == 26:
                break

        # sentence contains all characters if set contains all characters
        return len(chars) == 26

    def checkIfPangram_lazy(self, sentence: str) -> bool:
        # O(n) / O(1)   time / space complexity
        return len(set(sentence)) == 26
