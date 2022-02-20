class cheatBSTIterator:
    def __init__(self, root: TreeNode):
        def dfs(root):
            if root:
                dfs(root.left)
                self.list.append(root.val)
                dfs(root.right)
        self.list = []
        dfs(root)
        self.idx = -1
        self.len = len(self.list)

    def next(self) -> int:
        self.idx += 1
        return self.list[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < self.len


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        lowest = self.stack.pop()
        self.push_left(lowest.right)
        return lowest.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
