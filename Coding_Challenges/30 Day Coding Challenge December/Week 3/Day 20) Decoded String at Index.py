def decodeAtIndex(self, S: str, K: int) -> str:
    curMult = 0
    fullStr = ""
    for c in S:
        if c.isdigit():
            curMult = curMult * 10 + int(c)
            if curMult * len(fullStr) > K:
                return fullStr[(curMult * len(fullStr)) % K]
        elif curMult:
            fullStr = fullStr * curMult
        elif len(fullStr) == K:
            return c
        else:
            fullStr += c


x = decodeAtIndex(0, "leet2code3", 10)
print(x)
