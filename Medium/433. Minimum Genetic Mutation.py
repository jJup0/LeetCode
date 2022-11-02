from typing import List


class Solution:
    """
    A gene string can be represented by an 8-character long string, with choices from 'A', 'C',
    'G', and 'T'.

    Suppose we need to investigate a mutation from a gene string start to a gene string end where
    one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
    There is also a gene bank bank that records all the valid gene mutations. A gene must be in
    bank to make it a valid gene string.

    Given the two gene strings start and end and the gene bank bank, return the minimum number of
    mutations needed to mutate from start to end. If there is no such a mutation, return -1.

    Note that the starting point is assumed to be valid, so it might not be included in the bank.

    Constraints:
        start.length == 8
        end.length == 8
        0 <= bank.length <= 10
        bank[i].length == 8
        start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
    """

    def minMutation_char_replace(self, start: str, end: str, bank: List[str]) -> int:
        """
        Idea taken from other submissions. Don't compare string pairwise, list all permutation and
        check if they are in the remaining bank.
        O(n * k) / O(n * k)     time / space complexity
        """

        # similar setup to original solution, see comments there

        bfs_front = [start]
        res = 0
        unused = set(bank)
        while bfs_front:
            next_front = []
            res += 1
            for gene in bfs_front:
                # perform all possible mutations
                for pos in range(8):
                    for c in 'ACGT':
                        mutation = gene[:pos] + c + gene[pos+1:]
                        if mutation in unused:
                            if mutation == end:
                                return res
                            unused.remove(mutation)
                            next_front.append(mutation)

            bfs_front = next_front

        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        No need to optimize for performance, genes only 8 chars long, bank has max 10 genes.
        k:= length of genes
        #O(n^2 * k) / O(n * k)      time / space complexity
        """

        # remaining permutations not yet used
        remaining = set(bank)

        # if end cannot be reached, return -1 immediately
        if end not in remaining:
            return -1

        # result variable
        res = 0

        # set of genes in current bfs mutation
        front = set([start])
        while front:
            res += 1
            # bfs front for next iteration
            next_front = set()
            for gene in front:
                # check for all unused genes if a mutation is possible, i.e. character difference
                # is less than 2
                for gene2 in tuple(remaining):
                    diff = 0
                    for c1, c2 in zip(gene, gene2):
                        diff += c1 != c2
                        if diff == 2:
                            break
                    # if mutation possible, remove from genebank and add to bfs front, return early
                    # if end gene is found
                    if diff < 2:
                        if gene2 == end:
                            return res
                        next_front.add(gene2)
                        remaining.remove(gene2)

            front = next_front

        # no sequence of mutations found, return 0
        return -1
