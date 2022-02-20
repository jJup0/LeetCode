class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        return [word for word in words if (ws := set(word)).issubset(row1) or ws.issubset(row2) or ws.issubset(row3)]
