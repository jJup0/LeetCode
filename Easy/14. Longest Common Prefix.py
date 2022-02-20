class firstSolution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ''

        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        lenShortestWord = 2**31
        for s in strs:
            lenS = len(s)
            if lenS < lenShortestWord:
                lenShortestWord = lenS
        if not lenShortestWord:
            return ''

        for l in range(lenShortestWord):
            w = 1
            while w < len(strs):
                if strs[w][l] != strs[0][l]:
                    return r
                w += 1
            r += strs[0][l]
        return r  # whole word is prefix


class shortSolution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()  # sorted alphabetically. if they share a prefix, the last item is possibly the most complex e.g: abc, abcd, abcqifspi
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                p += x
            else:
                break
        return p
