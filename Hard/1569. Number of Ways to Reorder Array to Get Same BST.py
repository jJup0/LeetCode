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
        self.self_plus_descendents_count = 1

    def add_val_node_bst(self, val: int):
        """Adds a value as a node in BST fashion."""
        self.self_plus_descendents_count += 1
        if val < self.val:
            if self.left:
                self.left.add_val_node_bst(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.add_val_node_bst(val)
            else:
                self.right = TreeNode(val)

    def __repr__(self) -> str:
        return f"TN{'{'}{self.val}{'}'}"


class UnlimitedFactorial:
    """Provides armortized O(1) factorial values."""

    def __init__(self) -> None:
        self.factorials = [1]

    def __getitem__(self, i: int):
        while i >= len(self.factorials):
            self.factorials.append(self.factorials[-1] * len(self.factorials))
        return self.factorials[i]


class Solution:
    """
    Given an array nums that represents a permutation of integers from 1 to n.
    We are going to construct a binary search tree (BST) by inserting the elements
    of nums in order into an initially empty BST. Find the number of different ways
    to reorder nums so that the constructed BST is identical to that formed from
    the original array nums.

    - For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left
      child, and 3 as a right child. The array [2,3,1] also yields the same BST
      but [3,2,1] yields a different BST.

    Return the number of ways to reorder nums such that the BST formed is
    identical to the original BST formed from nums.

    Since the answer may be very large, return it modulo 10^9 + 7.

    Constraints:
    - 1 <= nums.length <= 1000
    - 1 <= nums[i] <= nums.length
    - All integers in nums are distinct.
    """

    def numOfWays(self, nums: list[int]) -> int:
        root = TreeNode(nums[0])
        self.factorials = UnlimitedFactorial()
        # build a BST
        for i in range(1, len(nums)):
            root.add_val_node_bst(nums[i])
        # get permutations for root, subtract 1 to get reorderings of original permutation
        return (self._get_permutation_count(root) - 1) % (10**9 + 7)

    def _get_permutation_count(self, node: TreeNode) -> int:
        if not node.left and not node.right:
            # only one permutation exists to construct a leaf node
            return 1

        if not node.left or not node.right:
            # a node with only one child can only be constructed by starting with
            # the node, and then the permutations that construct the child
            res = self._get_permutation_count(node.left or node.right)  # type: ignore # one with not be none
            return res

        # interleaving the possible permutations for two set of numbers is equal to:
        # x * y * (x+y choose x) == x * y * (x+y choose y)
        # because the left nodes can be permuted x-ways, for each permutation
        # the right nodes can permute y times, and for each of those permutations
        # they can be interleaved (x+y choose x) different ways
        l_count = self._get_permutation_count(node.left)
        r_count = self._get_permutation_count(node.right)
        res = (
            l_count
            * r_count
            * self._n_choose_k(
                node.left.self_plus_descendents_count
                + node.right.self_plus_descendents_count,
                node.right.self_plus_descendents_count,
            )
        )
        return res

    def _n_choose_k(self, n: int, k: int) -> int:
        return self.factorials[n] // (self.factorials[k] * self.factorials[n - k])
