class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        def traverse_mdll(node, prevnode=None, fromQueueORchild=False):
            if not node:
                return
            if fromQueueORchild:
                node.prev = prevnode
            if node.child:
                nodequeue.append(node.next)
                node.next = node.child
                traverse_mdll(node.child, node, True)
                node.child = None
            else:
                traverse_mdll(node.next, node)
                if nodequeue:
                    node.next = nodequeue.pop()
                    traverse_mdll(node.next, node, True)

        nodequeue = []
        traverse_mdll(head)
        return head
