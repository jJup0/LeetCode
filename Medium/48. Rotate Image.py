from typing import List


class Solution:
    # in place
    def rotate(self, matrix: List[List[int]]) -> None:
        n_dec = len(matrix) - 1

        # image of size n has n//2 "rings"
        for ring in range(len(matrix)//2):
            # a ring can be broken up into 4 segments, each of length n - 1 - ring_idx * 2
            for step in range(ring, n_dec-ring):
                left_top = matrix[ring][step]
                right_top = matrix[step][n_dec-ring]
                right_bottom = matrix[n_dec-ring][n_dec-step]
                left_bottom = matrix[n_dec-step][ring]

                matrix[ring][step] = left_bottom
                matrix[step][n_dec-ring] = left_top
                matrix[n_dec-ring][n_dec-step] = right_top
                matrix[n_dec-step][ring] = right_bottom
