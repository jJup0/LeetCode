from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # base case
        if not head:
            return None

        # clone head
        clone_pointer = head_clone = Node(head.val)

        # construct dictionary where original node map to their clones
        original_to_clone = {head: clone_pointer}

        # traverse through list creating clones and storing original to clone mapping
        old_pointer = head.next
        while old_pointer:
            clone_pointer.next = Node(old_pointer.val)
            clone_pointer = clone_pointer.next

            original_to_clone[old_pointer] = clone_pointer
            old_pointer = old_pointer.next

        # second pass to add .random to clones
        old_pointer = head
        while old_pointer:
            # retrieve cloned version of current node
            cloned_node = original_to_clone[old_pointer]
            # if random pointer is not None then...
            original_random = old_pointer.random
            if original_random:
                # retrive its clone counter part and add to .random of current clone
                cloned_node.random = original_to_clone[original_random]
            old_pointer = old_pointer.next

        return head_clone
