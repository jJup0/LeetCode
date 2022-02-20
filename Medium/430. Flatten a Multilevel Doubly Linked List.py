# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def traverse_mdll(node, prevnode, fromQueueORchild):
            if not node:
                return
            if fromQueueORchild:
                node.prev = prevnode
            if node.child:
                nodequeue.append(node.next)
                node.next = node.child
                traverse_mdll(node.next, node, True)
                node.child = None
            else:
                traverse_mdll(node.next, node, False)
                if nodequeue:
                    node.next = None
                    while nodequeue and node.next == None:
                        node.next = nodequeue.pop()
                    traverse_mdll(node.next, node, True)

        nodequeue = []
        traverse_mdll(head, None, False)
        return head
