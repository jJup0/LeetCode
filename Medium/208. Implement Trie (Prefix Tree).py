class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure used to
    efficiently store and retrieve keys in a dataset of strings. There are various
    applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
        void insert(String word) Inserts the string word into the trie.
        boolean search(String word) Returns true if the string word is in the trie
            (i.e., was inserted before), and false otherwise.
        boolean startsWith(String prefix) Returns true if there is a previously inserted
            string word that has the prefix prefix, and false otherwise.

    Constraints:
        1 <= word.length, prefix.length <= 2000
        word and prefix consist only of lowercase English letters.
        At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
    """

    def __init__(self):
        # O(1) time complexity
        # tree root
        self.trie = {}

    def insert(self, word: str) -> None:
        # O(n) time complexity
        # pointer to current sub-trie
        curr = self.trie
        for c in word:
            # add letters of word to trie, make new sub-trie
            # if words with prefix have never been inserted
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        # add dummy terminating symbol at the end
        curr["$"] = None

    def search(self, word: str) -> bool:
        # O(n) time complexity
        # same procedure as in self.insert()
        curr = self.trie
        for c in word:
            # if prefix does not exist, return False
            if c not in curr:
                return False
            curr = curr[c]

        # only return true if terminating symbol
        # is a child of the current sub-trie
        return "$" in curr

    def startsWith(self, prefix: str) -> bool:
        # O(n) time complexity
        # same as self.search()
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        # return True regarless of whether terminating symbol in sub-trie
        return True
