from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # cCounter = Counter(s)
        # countDict = dict()
        # countOrder = set()
        # retVal = ''
        # for _key, _count in cCounter.items():
        #     countOrder.add(_count)
        #     if _count in countDict:
        #         countDict[_count].append(_key)
        #     else:
        #         countDict[_count] = [_key]
        # countOrder = sorted(list(countOrder), reverse=True)
        # for _count in countOrder:
        #     for c in countDict[_count]:
        #         retVal += c*_count
        # return retVal
        l = Counter(s)
        retVal = ''
        for char, count in (sorted(l.items(), key=lambda item: item[1], reverse=True)):  # sort dict items based on value (letter count)
            retVal += char*count
        return retVal
