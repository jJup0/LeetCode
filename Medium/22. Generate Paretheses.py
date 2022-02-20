class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        def backtrack(openB=0, openedB=0, curBseq=''):
            # print(curBseq)
            if openedB < n:
                backtrack(openB + 1, openedB + 1, curBseq + '(')
            if openB > 0:
                backtrack(openB - 1, openedB, curBseq + ')')
            if openB == 0 and openedB == n:
                result.append(curBseq)
        result = []
        backtrack()
        return result
