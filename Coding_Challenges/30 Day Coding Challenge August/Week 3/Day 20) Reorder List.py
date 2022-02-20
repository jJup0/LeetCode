# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         curnode = head
#         allNodes = []
#         while curnode:      #add all nodes to list
#             allNodes.append(curnode)
#             curnode = curnode.next
#         if len(allNodes) < 3:   #return if 2 or less nodes
#             return

#         dummy = head
#         i = len(allNodes) - 1
#         while i > len(allNodes)/2:      #merge last nodes into linked list
#             allNodes[i].next = dummy.next
#             dummy.next = allNodes[i]
#             dummy = allNodes[i].next
#             i -= 1
#         if len(allNodes) % 2:           #set last node.next to none
#             dummy.next.next.next = None
#         else:
#             dummy.next.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        # find middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half of list
        prev = None
        curr = slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge 2nd half with 1st half
        first, second = head, prev
        while second.next:  # insort node from second half between two first
            first.next, first = second, first.next
            second.next, second = first, second.next
