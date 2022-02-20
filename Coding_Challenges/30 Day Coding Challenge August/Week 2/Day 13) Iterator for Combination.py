class CombinationIterator:

    def __init__(self, characters: str, comboLen: int):
        self.curidxs = [i for i in range(comboLen-1)]+[comboLen-2]
        self.comboLen = comboLen
        self.characters = characters

    def next(self) -> str:
        # i = len(self.curidxs) - 1
        # while i >= 0:
        #     if self.curidxs[i] != i+1:
        #         break
        #     i -= 1
        for i, curIdx in enumerate(self.curidxs[::-1]):
            if curIdx != len(self.characters)-i-1:
                break
        i = self.comboLen-1-i
        self.curidxs[i] += 1
        for j in range(i+1, self.comboLen):
            self.curidxs[j] = self.curidxs[j-1]+1
        return (''.join(self.characters[i] for i in self.curidxs))

    def hasNext(self) -> bool:
        return self.curidxs != [i for i in range(len(self.characters)-self.comboLen, len(self.characters))]


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
