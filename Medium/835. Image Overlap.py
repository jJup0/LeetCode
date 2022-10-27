from collections import Counter
from typing import List


class Solution:
    """
    You are given two images, img1 and img2, represented as binary, square matrices of size n x n.
    A binary matrix has only 0s and 1s as values.

    We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down
    any number of units. We then place it on top of the other image. We can then calculate the 
    overlap by counting the number of positions that have a 1 in both images.

    Note also that a translation does not include any kind of rotation. Any 1 bits that are
    translated outside of the matrix borders are erased.

    Return the largest possible overlap.

    Constraints:
        n == img1.length == img1[i].length
        n == img2.length == img2[i].length
        1 <= n <= 30
        img1[i][j] is either 0 or 1.
        img2[i][j] is either 0 or 1.
    """

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        O(n^4) / O(n^2)     time / space complexity
        """
        n = len(A)

        # get all the coordinates of 1's in both matrices
        pos_of_1_in_A = tuple((x, y) for x in range(n) for y in range(n) if A[x][y])
        pos_of_1_in_B = tuple((x, y) for x in range(n) for y in range(n) if B[x][y])

        # calculate the offset between every coordinate in a, with every coordinate in b, and store these in a counter
        offset_counter = Counter((x_a - x_b, y_a - y_b)
                                 for (x_a, y_a) in pos_of_1_in_A
                                 for (x_b, y_b) in pos_of_1_in_B)

        # the key to the highest value in num responds to the shift with the highest overlap
        # if either matrix does not contain any ones, counter could be empty so return 0
        return max(offset_counter.values(), default=0)

    def largestOverlap_bits(self, _A: List[List[int]], _B: List[List[int]]) -> int:
        """
        O(n^3 * complexity_of_bitcount) / O(n^2)    time / space complexity
        """
        n = len(_A)

        # convert matrices into bit matrices
        A = []
        B = []
        for i in range(n):
            row_a = row_b = 0
            for j in range(n):
                row_a |= (1 << j) * _A[i][j]
                row_b |= (1 << j) * _B[i][j]
            A.append(row_a)
            B.append(row_b)

        res = 0

        # iterate through all possible row and col offsets
        for row_offset in range(n):
            # calculate row shifted matrices in O(n) assuming >> is constant
            B_shift_down = [col >> row_offset for col in B]
            B_shift_up = [col << row_offset for col in B]

            for col_offset in range(n):
                # calculate overlaps for both offsets in both directions

                # overlap counters, names refer to how B is shifted compared to A
                down_right = down_left = up_right = up_left = 0
                
                # iterate through columns remaining after shift to calculate overlap
                for col in range(col_offset, n):
                    right_shifted_col = col - col_offset
                    down_right += (A[col] & B_shift_down[right_shifted_col]).bit_count()
                    down_left += (A[right_shifted_col] & B_shift_down[col]).bit_count()
                    up_right += (A[col] & B_shift_up[right_shifted_col]).bit_count()
                    up_left += (A[right_shifted_col] & B_shift_up[col]).bit_count()

                # update res if any of the shifts achieved higher overlap
                res = max(res, down_right, up_right, down_left, up_left)

        return res
