class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if len(word) == 1:
        #     return True
        # capitalized = True if word[0].isupper() else False
        # allCaps = True if word[1].isupper() else False
        # if not capitalized and allCaps:
        #     return False
        # for c in word[2:]:
        #     if c.isupper() != allCaps:
        #         return False
        # return True
        return word in (word.upper(), word.lower(), word.capitalize())
