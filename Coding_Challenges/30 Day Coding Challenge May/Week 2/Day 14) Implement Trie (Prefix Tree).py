class Trie:
    def __init__(self):
        # self.wset = set()
        self.cdict = dict()

    def insert(self, word: str) -> None:
        # self.wset.add(word)
        curdict = self.cdict
        for c in word:
            if not(c in curdict):
                curdict[c] = dict()
            curdict = curdict[c]
        curdict['.'] = None

    def search(self, word: str) -> bool:
        # return word in self.wset
        curdict = self.cdict
        for c in word:
            if c in curdict:
                curdict = curdict[c]
            else:
                return False
        return '.' in curdict

    def startsWith(self, prefix: str) -> bool:
        curdict = self.cdict
        for c in prefix:
            if c in curdict:
                curdict = curdict[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
