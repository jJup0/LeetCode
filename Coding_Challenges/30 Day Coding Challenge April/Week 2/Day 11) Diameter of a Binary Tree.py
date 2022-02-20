class hellaComplexAlmostWorkedSolution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def findDepth(node, curDepth=0, nodeNav='', maxDepthNode=root, maxDepth=0, maxDepthNav=''):
            if node:
                # print(node.val, end='with maxdepth')
                if curDepth > maxDepth:
                    maxDepth = curDepth
                    maxDepthNode = node
                    maxDepthNav = nodeNav
                # print('maxNav = ' + maxDepthNav)
                curDepth += 1
                d1, n1, nn1 = findDepth(node.left, curDepth, nodeNav+'l', maxDepthNode, maxDepth, maxDepthNav)
                d2, n2, nn2 = findDepth(node.right, curDepth, nodeNav+'r', maxDepthNode, maxDepth, maxDepthNav)
                if d1 > d2:
                    return (d1, n1, nn1)
                else:
                    return (d2, n2, nn2)
            return (maxDepth, maxDepthNode, maxDepthNav)
        # ************************************************************************************** #

        theMaxDepth, theMaxDepthNode, theMaxDepthNodeNav = findDepth(root)
        print('max d: ' + str(theMaxDepth))
        print('Max d nav: ' + theMaxDepthNodeNav)
        print("Searching for Opposite")
        # print(theMaxDepthNode.val)

        oppNode = oppNodeC = root
        tMDNN = theMaxDepthNodeNav
        maxOppDepth = 0
        if tMDNN:
            if tMDNN[0] == 'l':
                if oppNodeC.right:
                    maxOppDepth, _, _ = findDepth(oppNodeC.right, curDepth=1, maxDepth=1)
                    oppNode = oppNode.left
                    nodeNavStart = 'l'
            else:
                if oppNodeC.left:
                    maxOppDepth, _, _ = findDepth(oppNodeC.left, curDepth=1, maxDepth=1)
                    oppNode = oppNode.right
                    nodeNavStart = 'r'

            print('max org opp depth: ' + str(maxOppDepth))
            maxOppDepth1 = 0
            # for i in range(1, len(tMDNN) -1):
            print('1 to ' + str(round((len(tMDNN) - 1.1)/2)))
            for i in range(1, round((len(tMDNN) - 1.1)/2)):
                print('going for round ' + str(i))
                oppNodeC = oppNode
                # if maxOppDepth > theMaxDepth - i:
                #     break
                if tMDNN[i] == 'l':
                    if oppNodeC.right:
                        maxOppDepth1, _, mOP1NN = findDepth(oppNodeC.right, curDepth=-i, maxDepth=-i)
                    oppNode = oppNode.left
                else:
                    if oppNodeC.left:
                        maxOppDepth1, _, mOP1NN = findDepth(oppNodeC.left, curDepth=-i, maxDepth=-i)
                    oppNode = oppNode.right
                print('maxoppdepth: ' + str(maxOppDepth1))
                print('maxoppd nav: ' + mOP1NN)
            maxOppDepth = max(maxOppDepth, maxOppDepth1)

        # ************************************************************************************** #

        print('final maxoppdepth: ' + str(maxOppDepth))
        return (maxOppDepth + theMaxDepth)


# dfs
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = 0

        def dfs(node):
            nonlocal d
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            d = max(d, l+r)
            return max(l, r)+1

        dfs(root)
        return d
