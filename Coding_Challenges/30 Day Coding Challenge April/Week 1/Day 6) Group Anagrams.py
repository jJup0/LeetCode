class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        anagramDict = dict()
        for string in strs:
            orderedString = ''.join(sorted(string))
            if orderedString in anagramDict:
                anagramDict[orderedString].append(string)
            else:
                anagramDict[orderedString] = [string]
        return anagramDict.values()
