class Solution:
    def checkValidString(self, s: str) -> bool:
        stillOpen, jokerPositions = [], []
        for i, char in enumerate(s):
            if char == '(':
                stillOpen.append(i)
            elif char == ')':
                if len(stillOpen):
                    stillOpen.pop()
                else:
                    if len(jokerPositions):
                        jokerPositions.pop()
                    else:
                        return False
            else:
                jokerPositions.append(i)

        while stillOpen and jokerPositions:
            if stillOpen.pop() > jokerPositions.pop():
                return False
        return not stillOpen
