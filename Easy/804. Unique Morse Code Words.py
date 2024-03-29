from typing import List


class Solution:
    """
    International Morse Code defines a standard encoding where each letter is mapped to a series of
    dots and dashes, as follows:
        'a' maps to ".-",
        'b' maps to "-...",
        'c' maps to "-.-.", and so on.
    For convenience, the full table for the 26 letters of the English alphabet is given below:
        [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",
        ".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    Given an array of strings words where each word can be written as a concatenation of the Morse
    code of each letter.
    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-",
    and "-...". We will call such a concatenation the transformation of a word.
    Return the number of different transformations among all words we have.
    Constraints:
        1 <= words.length <= 100
        1 <= words[i].length <= 12
        words[i] consists of lowercase English letters.
    """

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Create a set of all words translated to morse and return its length.
        O(n) / O(n)     time / space complexity
        """

        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        ord_a = ord('a')
        return len({''.join(morse[ord(c) - ord_a] for c in word) for word in words})
