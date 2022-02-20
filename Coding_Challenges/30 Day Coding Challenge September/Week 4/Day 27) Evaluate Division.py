from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divDict = defaultdict(list)
        for pair, val in zip(equations, values):
            divDict[pair[0]].append((pair[1], val))
            divDict[pair[1]].append((pair[0], 1/val))

        def dfs(visited, curLetter, goal, curFactor):
            if curLetter == goal and curLetter in divDict:
                return curFactor
            connectedLetters = divDict.get(curLetter)
            if connectedLetters == None:
                return -1
            else:
                visited.add(curLetter)
                for B, factor in connectedLetters:
                    if not B in visited and (res := dfs(visited, B, goal, curFactor * factor)):
                        return res

        retList = [-1] * len(queries)
        for i, pair in enumerate(queries):
            if res := dfs(set(), pair[0], pair[1], 1):
                retList[i] = res

        return retList
