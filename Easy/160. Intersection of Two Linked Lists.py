# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given the heads of two singly linked-lists headA and headB, return the node at which the
    two lists intersect. If the two linked lists have no intersection at all, return null.
    For example, the following two linked lists begin to intersect at node c1:
    https://assets.leetcode.com/uploads/2021/03/05/160_statement.png
    The test cases are generated such that there are no cycles anywhere in the entire linked structure.
    Note that the linked lists must retain their original structure after the function returns.
    Constraints:
        The number of nodes of listA is in the m.
        The number of nodes of listB is in the n.
        1 <= m, n <= 3 * 10^4
        1 <= Node.val <= 10^5
        0 <= skipA < m
        0 <= skipB < n
        intersectVal is 0 if listA and listB do not intersect.
        intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
    """
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(2*m + n) time, O(1) space
        """
        # constraint states every node value is positive, mark nodes as part of A by making them 
        # negative, then invert again before returning, to leave list unmodified
        def invert_A():
            curr_a = headA
            while curr_a:
                curr_a.val = -curr_a.val
                curr_a = curr_a.next
        
        invert_A()
        
        # find the first negative value that is now part of b, this is where they intersect
        # if no negative value is found, ret will be null, which it should be by specification
        ret = headB
        while ret and ret.val > 0:
            ret = ret.next
        
        # repair A as it should remain unmodified at the end
        invert_A()
            
        return ret
        
        
# # other solution that does not rely on positive values constraint, but in my opinion not good in worst case
# # consider two lists without intersection and of extreme length n, with a length difference of 1 it
# # will take n(n-1) (~n^2) iterations for both pointers to land at null, as n and n-1 share no factors
#     if(headA is None or headB is None):
#         return None
#     a=headA
#     b=headB
#     while(a != b): # will both at least be null at some point
#         a = headB if a is None else a.next
#         b = headA if b is None else b.next
#     return a