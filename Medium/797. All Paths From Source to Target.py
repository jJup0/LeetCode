class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def traverseGraph(curPath, curI):
            for nextNode in graph[curI]:
                if nextNode == m:
                    retList.append(curPath + [nextNode])
                else:
                    traverseGraph(curPath + [nextNode], nextNode)
        retList, m = [], len(graph) - 1
        traverseGraph([0], 0)
        return retList
