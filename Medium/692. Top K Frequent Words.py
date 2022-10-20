import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        O(n * log(k)) / O(k)    time / space complexity
        """

        # O(n) / O(n) time / space
        # create a counter of the words
        c = Counter(words)

        # O(n * log(k)) / O(k) time / space
        # get the most often occuring words. Since the question specifies that for equal occurances
        # the strings must be in lexographical order, use nsmallest with sorting by negative count
        # and then string. Less intuitive than nlargest, but there is no way to "negate" a string,
        # to sort by strings descending
        largest = heapq.nsmallest(k, c.items(), key=lambda x: (-x[1], x[0]))

        # O(k) / O(1)   time / extra space
        # return only the words from the largest
        return [w for w, _ in largest]
