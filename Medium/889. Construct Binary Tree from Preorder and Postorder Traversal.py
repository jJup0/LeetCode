"""
Given two integer arrays, preorder and postorder where preorder is the preorder
traversal of a binary tree of distinct values and postorder is the postorder
traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Constraints:
- 1 <= preorder.length <= 30
- 1 <= preorder[i] <= preorder.length
- All the values of preorder are unique.
- postorder.length == preorder.length
- 1 <= postorder[i] <= postorder.length
- All the values of postorder are unique.
- It is guaranteed that preorder and postorder are the preorder traversal and
  postorder traversal of the same binary tree.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode | None" = None,
            right: "TreeNode | None" = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution1:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode:
        """First implementation, somewhat clumsy, aims to simulate
        construction of tree with pre and post order values.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.preorder = preorder
        self.postorder = postorder
        self.pre_idx = 1
        self.post_idx = 0
        root = TreeNode(preorder[0])
        self._construct(root)
        return root

    def _construct(self, node: TreeNode):
        if node.val == self.postorder[self.post_idx]:
            self.post_idx += 1
            return
        child_val = self.preorder[self.pre_idx]
        node.left = TreeNode(child_val)
        self.pre_idx += 1
        self._construct(node.left)

        if node.val == self.postorder[self.post_idx]:
            self.post_idx += 1
            return
        child_val = self.preorder[self.pre_idx]
        node.right = TreeNode(child_val)
        self.pre_idx += 1
        self._construct(node.right)

        assert node.val == self.postorder[self.post_idx]
        self.post_idx += 1
        return


class Solution2:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        """Array slicing divide and conquer approach.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        if not postorder:
            return None
        val = postorder.pop()
        node = TreeNode(val)
        if not postorder:
            return node

        left_val = preorder[1]
        left_val_post_order_index = postorder.index(left_val)
        left_last_descendant_pre_order_index = left_val_post_order_index + 2
        node.left = self.constructFromPrePost(
            preorder[1:left_last_descendant_pre_order_index],
            postorder[: left_val_post_order_index + 1],
        )
        node.right = self.constructFromPrePost(
            preorder[left_last_descendant_pre_order_index:],
            postorder[left_val_post_order_index + 1 :],
        )
        return node


class Solution3:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode:
        """Cleaner more direct implementation of Solution1.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.preorder = preorder
        self.postorder = postorder
        self.pre_idx = 0
        self.post_idx = 0
        return self._construct()

    def _construct(self) -> TreeNode:
        # create node and increment preorder index
        root = TreeNode(self.preorder[self.pre_idx])
        self.pre_idx += 1

        # before recursing to children, check if root has become the
        # current node in post order, then do not recurse
        if root.val != self.postorder[self.post_idx]:
            root.left = self._construct()
            if root.val != self.postorder[self.post_idx]:
                root.right = self._construct()

        assert root.val == self.postorder[self.post_idx]
        # increment post order index
        self.post_idx += 1
        return root


class Solution(Solution3):
    pass


def test():
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    res = Solution().constructFromPrePost(pre, post)
    res3 = Solution3().constructFromPrePost(pre, post)
    print(res)
    print(res3)


test()
