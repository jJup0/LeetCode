from typing import List


class Solution:
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
    (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix
    directly. DO NOT allocate another 2D matrix and do the rotation.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        O(n^2) / O(1)     time / space complexity
        """
        n_dec = len(matrix) - 1

        # rotate one ring at a time, image of size n has n//2 "rings"
        for ring in range(len(matrix)//2):
            # a ring can be broken up into 4 segments, each of length n - 1 - ring_idx * 2
            for step in range(ring, n_dec-ring):
                # temp store top left cell
                top_left = matrix[ring][step]
                
                # bottom left to top left
                matrix[ring][step] = matrix[n_dec-step][ring]
                
                # bottom right to bottom left
                matrix[n_dec-step][ring] = matrix[n_dec-ring][n_dec-step] 

                # top right to bottom right
                matrix[n_dec-ring][n_dec-step]= matrix[step][n_dec-ring]

                # top left to bottom right
                matrix[step][n_dec-ring] = top_left

