# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# constant space
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # O(n) space
        def dfs(root):
            if not root:
                return
            valCounter[root.val] = valCounter.get(root.val, 0) + 1
            dfs(root.left)
            dfs(root.right)

        valCounter = dict()
        dfs(root)
        pm = max(valCounter.values())
        return [val for val, count in valCounter.items() if count == pm]
