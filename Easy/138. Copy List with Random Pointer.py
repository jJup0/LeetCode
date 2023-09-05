from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    # Definition for a Node.
    class Node:
        def __init__(
            self, x: int, next: "Node" | None = None, random: "Node" | None = None
        ):
            self.val = int(x)
            self.next = next
            self.random = random


class Solution:
    """
    A linked list of length n is given such that each node contains an additional
    random pointer, which could point to any node in the list, or null.

    Construct a deep copy of the list. The deep copy should consist of exactly n
    brand new nodes, where each new node has its value set to the value of its
    corresponding original node. Both the next and random pointer of the new nodes
    should point to new nodes in the copied list such that the pointers in the
    original list and copied list represent the same list state. None of the
    pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes X and Y in the original list, where
    X.random --> Y, then for the corresponding two nodes x and y in the copied list,
    x.random --> y.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of n nodes. Each
    node is represented as a pair of [val, random_index] where:
    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random
      pointer points to, or null if it does not point to any node.

    Your code will only be given the head of the original linked list.

    Constraints:
    - 0 <= n <= 1000
    - -10^4 <= Node.val <= 10^4
    - Node.random is null or is pointing to some node in the linked list.
    """

    def copyRandomList(self, head: "Node | None") -> "Node | None":
        """
        Use dict to map from original node to copy.
        O(n) / O(n)     time / space complexity
        """
        # if the list is empty, return an empty list
        if head is None:
            return None

        # a mapping from the original nodes in the list to their copies
        original_to_copy: dict[Node | None, Node | None] = {None: None}

        # first create a copy of each node, by visiting each node's next node
        curr = head
        while curr:
            original_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # then for each copied node, add the .next and .random pointer to the respective copies
        curr = head
        while curr:
            node_copy = cast(Node, original_to_copy[curr])
            node_copy.next = original_to_copy[curr.next]
            node_copy.random = original_to_copy[curr.random]
            curr = curr.next

        # return the copy of the head of the list
        return original_to_copy[head]
