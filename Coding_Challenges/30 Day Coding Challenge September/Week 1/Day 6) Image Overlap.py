from collections import Counter


class Solution:
    def largestOverlap(self, A: [[int]], B: [[int]]):
        N = len(A)

        # position of 1 in matrix A: O(n*m)
        ones_in_A = [(xi, yi) for xi in range(N) for yi in range(N) if A[xi][yi]]

        # position of 1 in matrix B: O(n*m)
        ones_in_B = [(xi, yi) for xi in range(N) for yi in range(N) if B[xi][yi]]

        # counter for all possible x, y offsets for each 1 in A to each 1 in B. Time compl: O(n^2)
        offset_vector_counting = Counter([(x1 - x2, y1 - y2) for (x1, y1) in ones_in_A for (x2, y2) in ones_in_B])

        # the highest counting value is the largest overlap with most 1s: O(n)
        return max(offset_vector_counting.values() or (0, ))
