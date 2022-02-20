class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_set = set(ransomNote)
        for letter in ransom_set:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
