from collections import defaultdict
from typing import Dict, Iterable, List


class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any
    order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Constraints:
        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
    """

    def groupAnagrams(self, strs: List[str]) -> Iterable[List[str]]:
        """
        c := total number of characters in all strings 
        l := average length of string
        O(c * log(l)) / O(c)    time / space complexity
        """
        
        anagram_dict: Dict[str, List[str]] = defaultdict(list)
        for string in strs:
            # ordered version of a string is the same for each anagram
            orderedString = ''.join(sorted(string))

            # add current string to its respective list of anagrams
            anagram_dict[orderedString].append(string)

        # dictionary values are in the format needed
        return anagram_dict.values()
