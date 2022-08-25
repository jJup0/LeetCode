from collections import Counter


class Solution:
    """
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.
    Constraints:
        1 <= ransomNote.length, magazine.length <= 10^5
        ransomNote and magazine consist of lowercase English letters.
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 3.10 feature: rich comparison between Counters
        return Counter(ransomNote) <= Counter(magazine)

    def canConstruct_compatible(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        return all(r_counter[c] <= m_counter[c] for c in r_counter.keys())
