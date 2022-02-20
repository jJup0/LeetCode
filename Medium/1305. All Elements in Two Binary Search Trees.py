# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # faster to call sort() than to insort manually
        def inorder(root):
            if not root:
                return []
            ret = inorder(root.left)
            ret.append(root.val)
            ret.extend(inorder(root.right))
            return ret
        
        t = inorder(root1)
        t.extend(inorder(root2))
        t.sort()
        return t

        
        
#         tree1 = inorder(root1)
#         tree2 = inorder(root2)
#         ret = [0] * (len(tree1) + len(tree2))
#         i1 = i2 = 0
        
#         while i1 < len(tree1) and i2 < len(tree2):
#             int1 = tree1[i1]
#             int2 = tree2[i2]
#             if int1 < int2:
#                 ret[i1 + i2] = int1
#                 i1 += 1
#             else:
#                 ret[i1 + i2] = int2
#                 i2 += 1
            
        
#         if i1 == len(tree1):
#             ret[i1+i2:] = tree2[i2:]
#         else:
#             ret[i1+i2:] = tree1[i1:]
        
#         return ret

#         # tried recurive generator, very slow
#         def inorder_yielder(root):
#             if not root:
#                 return
#             yield from inorder_yielder(root.left)
#             yield root.val
#             yield from inorder_yielder(root.right)
        
#         t = list(inorder_yielder(root1))
#         t.extend(inorder_yielder(root2))
#         t.sort()
#         return t
                