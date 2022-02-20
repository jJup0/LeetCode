class Solution:
    def intervalIntersection(self, A: [[int]], B: [[int]]) -> [[int]]:
        R = []
        a_i, b_i = 0, 0
        while a_i < len(A) and b_i < len(B):
            if B[b_i][0] <= A[a_i][1] and B[b_i][1] >= A[a_i][0]:
                R.append([max(B[b_i][0], A[a_i][0]), min(B[b_i][1], A[a_i][1])])
            if B[b_i][1] < A[a_i][1]:
                b_i += 1
            elif A[a_i][1] < B[b_i][1]:
                a_i += 1
            else:
                a_i += 1
                b_i += 1
        return R
