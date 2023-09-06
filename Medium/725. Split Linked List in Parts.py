from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode" | None = None):
            self.val = val
            self.next = next


class Solution:
    """

    Given the head of a singly linked list and an integer k, split the linked list
    into k consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should
    have a size differing by more than one. This may lead to some parts being null.

    The parts should be in the order of occurrence in the input list, and parts
    occurring earlier should always have a size greater than or equal to parts
    occurring later.

    Return an array of the k parts.

    Constraints:
    - The number of nodes in the list is in the range [0, 1000].
    - 0 <= Node.val <= 1000
    - 1 <= k <= 50
    """

    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        # find length of the list
        len_pointer = head
        length = 0
        while len_pointer:
            length += 1
            len_pointer = len_pointer.next

        # find base length of every part and modulo
        # the first modulo parts will have one extra node
        base_part_len, modulo = divmod(length, k)

        res: list[ListNode | None] = []
        curr_node = head
        # iterate through list
        for i in range(k):
            if curr_node is None:
                # if the current node is ever None, then fill
                # the rest of res with None and break
                res.extend(None for _ in range(k - len(res)))
                break

            # save a pointer to the current node to add to result "array"
            curr_res = curr_node
            # make `base_part_len`-1 steps to the next node
            # if i is < modulo, then we make one extra step
            for _ in range(base_part_len - (i >= modulo)):
                curr_node = cast(ListNode, curr_node.next)

            # store a pointer to first node of the next part
            next_node = curr_node.next
            # cut off the current part from the rest of the list
            curr_node.next = None
            # update curr_node to next_node for the next iteration
            curr_node = next_node
            # append the current list part to the result "array"
            res.append(curr_res)

        return res
