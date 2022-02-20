class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [reversed([x ^ 1 for x in row]) for row in A]
