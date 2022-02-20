from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        l = Counter(s)
        retVal = ''
        for char, count in (sorted(l.items(), key=lambda item: item[1], reverse=True)):
            retVal += char*count
        return retVal
