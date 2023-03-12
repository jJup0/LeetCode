import heapq
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Constraints:
        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 10^4.
    """

    # monkey patch non existent __lt__ function, to make sortable in heap
    def __init__(self):
        setattr(ListNode, '__lt__', lambda x, y: x.val < y.val)

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Maintain min_heap of current smallest nodes of each list which has not been sorted in yet.
        O(total_nodes * log(k)) / O(k)    time / space complexity
        """

        # build a min-heap for all the heads of the linked lists
        next_candidates = [head for head in lists if head]
        heapq.heapify(next_candidates)

        # create a dummy head pointer, and maintain a pointer to the current tail of the merged list
        res_dummy = res_tail = ListNode()

        while next_candidates:
            # get the current smallest candidate
            smallest_node = heapq.heappop(next_candidates)

            # add it to the end of the merged list and update tail pointer
            res_tail.next = smallest_node
            res_tail = res_tail.next

            # add the successor of the smallest_node (if it exists) to the min heap of candidates
            if smallest_node.next:
                heapq.heappush(next_candidates, smallest_node.next)

        return res_dummy.next
