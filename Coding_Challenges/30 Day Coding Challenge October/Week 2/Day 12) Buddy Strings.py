class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if (len(A) != len(B)) or (not A):
            return False
        if A == B:
            return len(set(A)) < len(A)

        a_c1 = a_c2 = b_c1 = b_c2 = ""

        for c_a, c_b in zip(A, B):
            if c_a != c_b:
                if not a_c1:
                    a_c1, b_c1 = c_a, c_b
                elif not a_c2:
                    a_c2, b_c2 = c_a, c_b
                else:
                    return False

        return a_c1 == b_c2 and a_c2 == b_c1
