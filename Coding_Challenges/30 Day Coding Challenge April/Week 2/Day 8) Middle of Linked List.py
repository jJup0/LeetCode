class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        midPoint = 0.5
        curNode = head
        while curNode.next:
            curNode = curNode.next
            midPoint += 0.5
        midPoint = round(midPoint - 0.4)
        curNode = head
        for x in range(midPoint):
            curNode = curNode.next
        return curNode

