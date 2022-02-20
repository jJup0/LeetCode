# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        prev = set()
        while head:
            head_id = id(head)
            if head_id in prev:
                return head
            prev.add(head_id)
            head = head.next
        return None

    # def detectCycle2(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return None
    #     slow = head
    #     fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             break
    #     if not fast or not fast.next:
    #         return None
    #     second_slow = head
    #     while second_slow != slow:
    #         second_slow = second_slow.next
    #         slow = slow.next
    #     return slow
