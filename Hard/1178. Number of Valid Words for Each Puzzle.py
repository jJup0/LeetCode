from typing import List


class Solution:
    # explanation from https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/372145/Python-Bit-manipulation-detailed-explanation
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        # generates bitmask for word, eg mask for aelp
        # 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 1
        # z y x w v u t s r q p o n m l k j i h g f e d c b a
        def getBitMask(word: str) -> int:
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - ord('a')
            return mask

        wordBitMasks = Counter(getBitMask(w) for w in words)
        # wordBitMasks = Counter(functools.reduce(lambda mask, c : mask | (1 << ord(c) - ord('a')), w, 0) for w in words) # slower

        res = [0]*len(puzzles)
        for i, puzzle in enumerate(puzzles):

            # mask of first char of puzzle, needs to be in word
            p0mask = 1 << ord(puzzle[0]) - ord('a')

            # iterate through every submask of p instead of every element in wordBitMasks
            psubmask = pmask = getBitMask(puzzle)

            # count for how many words have fit puzzle so far
            total = 0

            while psubmask != 0:    # exhausted all submasks
                # if this submask contains the first letter of puzzle,
                # get the words that exactly fit this submask
                if psubmask & p0mask:
                    total += wordBitMasks.get(psubmask, 0)

                # bit hack to get next submask. in binary (val - 1) flips rightmost set bit in val to 0
                # and all following bits are set to 1. '&' the result with the mask to get a valid submask
                psubmask = (psubmask - 1) & pmask

            res[i] = total

        return res


# tried trie but was really broken

#         #slow
#         # wordsSet = list(set(word) for word in words)
#         ret = [0] * len(puzzles)
#         for i, puzzle in enumerate(puzzles):
#             # print(puzzle)
#             p0 = puzzle[0]
#             puzzle = set(puzzle)
#             for ws in wordsSet:
#                 if (p0 in ws) and ws.issubset(puzzle):
#                     ret[i] += 1
#         return ret
