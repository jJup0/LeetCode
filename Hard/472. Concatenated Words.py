from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable, Union


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:

        char_set_tree = {}
        sorted_char_set_dict = {}

        for word in words:
            sorted_char_set = ''.join(sorted(set(word)))
            sorted_char_set_dict[word] = sorted_char_set

            curr_tree = char_set_tree
            for c in sorted_char_set:
                if c not in curr_tree:
                    curr_tree[c] = {}
                curr_tree = curr_tree[c]
            
            if '$' not in curr_tree:
                curr_tree['$'] = set()

            curr_tree['$'].add(word)
            

        substr_idxs = {}

        # dfs through tree finding substrs
        MyTrie = dict[str, Union[set[str], 'MyTrie']]
        def dfs(curr_tree: MyTrie):
            word_set = [] # set()
            curr_level_words = []
            for c, t in sorted(curr_tree.keys()):
                # if c == '$':
                #     curr_level_words = curr_tree[c]
                # else:
                curr_word_set = dfs(curr_tree[c])
            
                x = 1
                for super_word in curr_word_set:
                    for sub_word in word_set:
                        # if len(word1) > len(word2):
                        #     word1, word2 = word2, word1
                        
                        find_start_idx = 0
                        while (idx := sub_word.find(super_word, find_start_idx)) != -1:
                            substr_idxs.setdefault(sub_word, {})
                            substr_idxs[sub_word].setdefault(find_start_idx, [])
                            substr_idxs[sub_word][find_start_idx].append(idx + len(word))
                            find_start_idx = idx + 1
                
                word_set.extend(curr_word_set)

            word_set.extend(curr_level_words)
            return word_set
        
        dfs(char_set_tree)
        print(len(substr_idxs))

        res = []
        for word, idxs in substr_idxs.items():
            curr_ends: set[int] = set((0,))
            for start, ends in sorted(idxs.items()):
                if start not in curr_ends:
                    continue
                curr_ends.update(ends)
            if (len(word)) in curr_ends:
                res.append(word)

        return res
        
            

        return []

    def findAllConcatenatedWordsInADict_slow(self, words: list[str]) -> list[str]:
        wd: dict[str, defaultdict[int, list[int]]] = {}
        for word in words:
            curr_idxs = defaultdict(list)
            for prev_word, prev_idxs in wd.items():
                find_start_idx = 0
                if len(word) < len(prev_word):
                    while (idx := prev_word.find(word, find_start_idx)) != -1:
                        prev_idxs[idx].append(idx + len(word))
                        find_start_idx = idx + 1
                else:
                    while (idx := word.find(prev_word, find_start_idx)) != -1:
                        curr_idxs[idx].append(idx + len(prev_word))
                        find_start_idx = idx + 1

            wd[word] = curr_idxs

        print(max(len(wd[w]) for w in wd))
        res = []
        for word, idxs in wd.items():
            curr_ends: set[int] = set((0,))
            for start, ends in sorted(idxs.items()):
                if start not in curr_ends:
                    continue
                curr_ends.update(ends)
            if (len(word)) in curr_ends:
                res.append(word)

        return res


S = Solution()
S.findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
