from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.word_len_dict = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.word_len_dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        m = len(word)
        for dict_word in self.word_len_dict[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False
