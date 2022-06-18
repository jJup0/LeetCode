from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    You are given the root of a binary tree. We install cameras on the tree nodes where each
    camera at a node can monitor its parent, itself, and its immediate children.
    Return the minimum number of cameras needed to monitor all nodes of the tree.
    Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        Node.val == 0
    """

    def minCameraCover_ownDP(self, root: Optional[TreeNode]) -> int:

        # enums for camera cover of current node
        COVERERED, NOT_COVERED, MUST_GET_CAMERA = 0x00, 0x01, 0x11

        # memoize cameras needed for nodes
        dp_with_camera = {}
        dp_without_camera = {}
        dp_without_camera_but_is_covered = {}

        # returns cameras needed to cover root
        def helper(root, cover_case):
            if not root:
                return 0x10 & cover_case

            # if node has children nodes
            if root.left or root.right:
                # first calculate dp for adding camera (needed for all 3 cover cases)
                if root not in dp_with_camera:
                    dp_with_camera[root] = helper(root.left, COVERERED) + helper(root.right, COVERERED) + 1

                # if the current node is covered
                if cover_case == COVERERED:
                    # calculate cameras needed if no extra camera is installed in current node
                    if root not in dp_without_camera_but_is_covered:
                        # children nodes are not covered by a camera, but do not need to have one themselves
                        dp_without_camera_but_is_covered[root] = helper(root.left, NOT_COVERED) + helper(root.right, NOT_COVERED)
                    # return minimum of installing and not installing at current node
                    res = min(dp_with_camera[root], dp_without_camera_but_is_covered[root])

                elif cover_case == MUST_GET_CAMERA:
                    # if this node has to have a camera, return the total cameras needed
                    res = dp_with_camera[root]

                else:  # cover_case == NO_COVER
                    # calculate the cameras needed if this node needs to be camera-covered by one of its children
                    if root not in dp_without_camera:
                        covered_by_left = helper(root.left, MUST_GET_CAMERA) + helper(root.right, NOT_COVERED)
                        covered_by_right = helper(root.left, NOT_COVERED) + helper(root.right, MUST_GET_CAMERA)
                        dp_without_camera[root] = min(covered_by_left, covered_by_right)
                    # return minimum between installing on node, or either child
                    res = min(dp_with_camera[root], dp_without_camera[root])
            else:
                # leaf node, needs camera only when not covered
                res = 0x1 & cover_case

            return res

        # start at root, which is not yet covered
        return helper(root, NOT_COVERED)

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        # enums for camera necessity of a node
        I_NEED_A_CAMERA = 0
        DO_NOT_NEED = -1
        I_AM_A_CAMERA = 1

        # returns a camera necessity code
        def resolve(node):
            # empty children do not need a camera
            if not node:
                return DO_NOT_NEED
            
            # find camera needs of children
            left = resolve(node.left)
            right = resolve(node.right)
            
            # if either child needs a camera, this node has to be a camera
            if left == I_NEED_A_CAMERA or right == I_NEED_A_CAMERA:
                self.count += 1
                return I_AM_A_CAMERA
            # if either child is a camera, this node does not need one
            elif left == I_AM_A_CAMERA or right == I_AM_A_CAMERA:
                return DO_NOT_NEED
            else:
            # if node is not a camera, and neither is either child, it needs a camera
                return I_NEED_A_CAMERA
        
        # if root needs a camera, parent node can not provide, so it needs to be a camera
        if resolve(root) == I_NEED_A_CAMERA:
            self.count += 1
            
        return self.count