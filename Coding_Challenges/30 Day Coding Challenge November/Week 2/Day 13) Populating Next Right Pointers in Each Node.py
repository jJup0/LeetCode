class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        currNode = root
        next_leftmost = currNode.left
        while currNode.left:
            currNode.left.next = currNode.right
            if currNode.next:  # this node has already been visited and is not on the very right
                currNode.right.next = currNode.next.left
                currNode = currNode.next
            else:  # we are done with this level, move to next
                currNode = next_leftmost
                next_leftmost = currNode.left
        return root
