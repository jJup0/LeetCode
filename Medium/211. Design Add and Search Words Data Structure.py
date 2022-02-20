from collections import defaultdict
class WordDictionary:
    # trie does not seem to be faster
    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            curr = curr.setdefault(c, {})
        curr['$'] = {}
        

    def search(self, word: str) -> bool:
        paths = [self.trie]
        for c in word:
            if c == '.':
                paths = [new_dict
                         for t in paths
                         for new_dict in t.values()]
            else:
                paths = [t[c]
                         for t in paths
                         if c in t]
        return any(t.get('$', None) == {} for t in paths)
    
class WordDictionary2:
    def __init__(self):  
        self.word_len_dict = defaultdict(set)

        
    def addWord(self, word: str) -> None:
        self.word_len_dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        self.word_len_dict[len(word)].add(word)
        m = len(word)
        for dict_word in self.word_len_dict[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False