from heapq import heapify, heappop, heappush
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # make ListNode sortable
    def __init__(self):
        setattr(ListNode, '__lt__', lambda x, y: x.val < y.val)

    # O(k) memory
    # O(n * log(k)) time
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a dummy node to return from
        dummy = curr = ListNode()

        # create a heap of all the contained lists that are not None, in O(k) time,
        # using O(k) space for the list, and then for the heap
        heap = list(node for node in lists if node)
        heapify(heap)

        # O(n * log(k)) time for n-k items to be pushed and n items to be popped, both operations in O(k) time
        while heap:
            # as long as there are nodes in the heap, pop one (smallest value in the heap)
            node = heappop(heap)

            # set that node as the next node, update curr
            # curr.next will always be overwritten from the previous node, and the last node added will
            # be the last node of one of the lists, so it will have None as its next node
            curr.next = node
            curr = curr.next

            # if the popped node has a next node, add it to the heap
            if node.next:
                heappush(heap, node.next)

        # return from dummy
        return dummy.next
