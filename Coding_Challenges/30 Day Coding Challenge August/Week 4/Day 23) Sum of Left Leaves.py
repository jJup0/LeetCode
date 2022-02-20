class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isLeft=False) -> int:
        if not root:
            return 0
        return (root.val * isLeft * int(not(bool(root.left) | bool(root.right)))) + self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
