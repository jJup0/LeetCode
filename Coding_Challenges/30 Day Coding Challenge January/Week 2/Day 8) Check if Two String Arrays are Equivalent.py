class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1) == "".join(word2)
        concat1 = concat2 = ""
        minLen = len(word1) if len(word1) < len(word2) else len(word2)

        for i in range(minLen):
            concat1 += word1[i]
            concat2 += word2[i]

            for c1, c2 in zip(concat1, concat2):
                if c1 != c2:
                    return False

            checked = min(len(concat1), len(concat2))
            concat1 = concat1[checked:]
            concat2 = concat2[checked:]

        return concat1 + ''.join(word1[minLen:]) == concat2 + ''.join(word2[minLen:])
