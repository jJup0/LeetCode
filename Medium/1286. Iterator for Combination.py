class CombinationIterator:

    def __init__(self, characters: str, comboLen: int):
        self.characters = characters
        self.comboLen = comboLen
        self.n = len(characters)

        # duplicate last value, as self.next() increments permutation *before* output
        self.curidxs = list(range(comboLen-1)) + [comboLen-2]

        # "highest" possible permutation that curidxs could be
        self.limit = list(range(self.n-self.comboLen, self.n))

    def next(self) -> str:

        # find lowest position, which is not at maximum possible value (for its position)
        for i, curIdx in enumerate(reversed(self.curidxs), start=1):
            if curIdx < self.n-i:
                break

        # actually get that position, since enumerated in reverse order
        i = self.comboLen-i
        # increment that position, to get next permutation
        self.curidxs[i] += 1

        # reset all indexes that were maxed, to be one higher than previous index
        self.curidxs[i+1:] = range(self.curidxs[i]+1, self.curidxs[i] + self.comboLen-i)
        # for j in range(i+1, self.comboLen):
        #     self.curidxs[j] = self.curidxs[j-1]+1

        return (''.join(self.characters[i] for i in self.curidxs))

    def hasNext(self) -> bool:
        return self.curidxs != self.limit


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
