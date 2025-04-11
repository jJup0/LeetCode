"""
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s_1 -> s_2 ->... -> s_k
such that:
- Every adjacent pair of words differs by a single letter.
- Every s_i for 1 <= i <= k is in wordList. Note that beginWord does not need
  to be in wordList.
- s_k == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord!= endWord
- All the words in wordList are unique.
"""

from collections import defaultdict


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        """
        Complexity:
            n := len(word_list)
            m := len(begin_word)
            a := length of the alphabet, in our case 26
            Time: O(n * m * m * a)
            Space: O(n * m * m)
        """
        try:
            end_word_idx = word_list.index(end_word)
        except ValueError:
            return 0
        try:
            begin_word_idx = word_list.index(begin_word)
        except ValueError:
            begin_word_idx = len(word_list)
            word_list.append(begin_word)

        word_idx_to_cuts, letter_cut_to_word_to_idxs = (
            self._create_adjacency_structures(begin_word, word_list)
        )

        # currently reachable words
        exploration_front = [begin_word_idx]
        # "visited" data structure
        added_to_front = [False] * len(word_list)
        added_to_front[begin_word_idx] = True
        # result variable
        words_in_chain_count = 1
        # bfs search for end word
        while exploration_front:
            words_in_chain_count += 1
            next_front: list[int] = []
            for word_idx in exploration_front:
                for neighbor_idx in self._unexplored_neighbors(
                    word_idx,
                    word_idx_to_cuts,
                    letter_cut_to_word_to_idxs,
                    added_to_front,
                ):
                    next_front.append(neighbor_idx)
                    added_to_front[neighbor_idx] = True
                    if neighbor_idx == end_word_idx:
                        return words_in_chain_count
            exploration_front = next_front
        # could not reach end_word from begin_word
        return 0

    def _unexplored_neighbors(
        self,
        word_idx: int,
        word_idx_to_cuts: list[list[str]],
        letter_cut_to_word_to_idxs: list[dict[str, list[int]]],
        added_to_front: list[bool],
    ):
        """
        Given the index of a word generate indexes of
        all words that have a one letter difference to this word.

        Complexity:
            Time: O(m * m * a)
            Space: O(1)
        """
        for cut_i, cut in enumerate(word_idx_to_cuts[word_idx]):
            for neighbor_idx in letter_cut_to_word_to_idxs[cut_i][cut]:
                if not added_to_front[neighbor_idx]:
                    yield neighbor_idx

    def _create_adjacency_structures(self, begin_word: str, word_list: list[str]):
        """
        Complexity:
            Time: O(n * m * m)
            Space: O(n * m * m)
        """
        # mapping from each word to its single letter removal slices
        word_idx_to_cuts = [
            [word[:i] + word[i + 1 :] for i in range(len(word))] for word in word_list
        ]
        # basically an inverse mapping of word_idx_to_cuts
        letter_cut_to_word_to_idxs: list[dict[str, list[int]]] = [
            defaultdict(list) for _ in range(len(begin_word))
        ]
        for word_i, cuts in enumerate(word_idx_to_cuts):
            for cut_i, cut in enumerate(cuts):
                letter_cut_to_word_to_idxs[cut_i][cut].append(word_i)
        return word_idx_to_cuts, letter_cut_to_word_to_idxs
