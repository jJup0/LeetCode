class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def doBackspace(S_T):
            retVal = ''
            curDeletes = 0
            for i in range(len(S_T) - 1, -1, -1):
                if S_T[i] == '#':
                    curDeletes += 1
                else:
                    if not curDeletes:
                        retVal += S_T[i]
                    else:
                        curDeletes -= 1
            return(retVal[::-1])

        return (doBackspace(S) == doBackspace(T))
