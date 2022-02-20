class Solution:
    def countNodes(self, root: TreeNode) -> int:
        #completely stolen        
        h = self.height(root)
        if h == -1:
            return 0
        if self.height(root.right) == h-1:
            return (1 << h) + self.countNodes(root.right)
        else:
            return (1 << h-1) + self.countNodes(root.left);

    def height(self, root: TreeNode):
        return 1 + self.height(root.left) if root else -1
        
        