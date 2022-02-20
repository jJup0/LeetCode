class Node():
    pass


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        stack = []
        while stack:
            newStack = []
            prev = Node()
            for node in stack:
                if node:
                    prev.next = node
                    prev = node
                    newStack.append(node.left)
                    newStack.append(node.right)

            stack = newStack
        return root
