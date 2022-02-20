class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        prevs = set()
        res = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in prevs:
                res.add(seq)
            else:
                prevs.add(seq)
        return res
