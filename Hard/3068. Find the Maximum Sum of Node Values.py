"""
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given
a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [u_i, v_i]
indicates that there is an edge between nodes u_i and v_i in the tree. You are
also given a positive integer k, and a 0-indexed array of non-negative integers
nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can
perform the following operation any number of times (including zero) on the tree:
- Choose any edge [u, v] connecting the nodes u and v, and update their values
  as follows:
  - nums[u] = nums[u] XOR k
  - nums[v] = nums[v] XOR k

Return the maximum possible sum of the values Alice can achieve by performing
the operation any number of times.

Constraints:
- 2 <= n == nums.length <= 2 * 10^4
- 1 <= k <= 10^9
- 0 <= nums[i] <= 10^9
- edges.length == n - 1
- edges[i].length == 2
- 0 <= edges[i][0], edges[i][1] <= n - 1
- The input is generated such that edges represent a valid tree.
"""

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    children: list["Node"]

    best_score_is_flipped = -1
    best_score_is_not_flipped = -1

    def get_best_score(self, k: int, is_flipped: bool) -> int:
        """
        Calculate best score for flipping node and its children.


        Args:
            k (int): Flipping XOR value
            is_flipped (bool): Whether this node has been flipped by its parent or not.

        Complexity:
            Time: O(n), amortized O(1)
            Space: O(n)
        """
        # check if value has already been calculated
        if is_flipped:
            if self.best_score_is_flipped != -1:
                return self.best_score_is_flipped
        else:
            if self.best_score_is_not_flipped != -1:
                return self.best_score_is_not_flipped

        children_scores = self._get_children_scores(k)

        # score which ends up not flipping this node's value
        score_no_flip = self.val + self._get_score_optimal_children_flip(
            children_scores.copy()
        )

        # score which ends up flipping this node's value
        _children_scores = children_scores.copy()
        if _children_scores:
            score_flip = (
                (self.val ^ k)
                + (_children_scores.pop()[0])
                + self._get_score_optimal_children_flip(_children_scores)
            )
        else:
            score_flip = -1

        res = max(score_flip, score_no_flip)
        if is_flipped:
            self.best_score_is_flipped = res
        else:
            self.best_score_is_not_flipped = res
        return res

    def _get_children_scores(self, k: int):
        for child in self.children:
            child.val ^= k
        children_scores_flip = [
            child.get_best_score(k, True) for child in self.children
        ]

        for child in self.children:
            child.val ^= k
        children_scores_no_flip = [
            child.get_best_score(k, False) for child in self.children
        ]

        children_scores = list(zip(children_scores_flip, children_scores_no_flip))
        children_scores.sort(key=lambda score_pair: score_pair[0] - score_pair[1])
        return children_scores

    def _get_score_optimal_children_flip(self, _children_scores: list[tuple[int, int]]):
        score = 0
        while len(_children_scores) >= 2:
            c1_flip, c1_no_flip = _children_scores.pop()
            c2_flip, c2_no_flip = _children_scores.pop()
            if c1_flip + c2_flip > c1_no_flip + c2_no_flip:
                score += c1_flip + c2_flip
            else:
                score += c1_no_flip + c2_no_flip
                break
        score += sum(c_score[1] for c_score in _children_scores)
        return score


class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """Construct tree and recursively find maximum value for subtrees.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        nodes = self._construct_tree(nums, edges)
        return nodes[0].get_best_score(k, False)

    def _construct_tree(self, nums: list[int], edges: list[list[int]]) -> list[Node]:
        n = len(nums)
        nodes = [Node(val, []) for val in nums]
        neighbor_nrs: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            neighbor_nrs[a].append(b)
            neighbor_nrs[b].append(a)

        visited = [False] * n
        front_nrs = [0]
        while front_nrs:
            node_nr = front_nrs.pop()
            visited[node_nr] = True
            for neighbor_nr in neighbor_nrs[node_nr]:
                if visited[neighbor_nr]:
                    continue
                nodes[node_nr].children.append(nodes[neighbor_nr])
                front_nrs.append(neighbor_nr)
        return nodes


class SimpleSolution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """Ignore tree structure, just find best nodes to XOR.

        Intution why this works:
            1. Find all nodes that have a higher value when XOR'ed.
               Assume there is an even count.
            2. Pair them up: (n1, n2), (n3, n4)...
            3. Find a path between them and apply the operation to every edge in
               this path. This XORs every node between the pair twice (no change)
               and the two nodes once, increasing their value.
            4. If there are an odd number of nodes that gain value when XOR'ed,
               simply ignore the smallest gain, or if the smallest loss is
               smaller than the smallest gain, then apply step 3 to those two
               nodes.

        Note that the graph does not have to be a tree for this to work, it just has to be connected.
        If not connected, can simply break up the problem and solve for each connected component.
        """
        total_score = 0
        node_count_for_XOR = 0
        smallest_diff_num_to_XORed = k

        for num in nums:
            xor_val = num ^ k
            if xor_val > num:
                total_score += xor_val
                node_count_for_XOR += 1
                smallest_diff_num_to_XORed = min(
                    smallest_diff_num_to_XORed, xor_val - num
                )
            else:
                total_score += num
                smallest_diff_num_to_XORed = min(
                    smallest_diff_num_to_XORed, num - xor_val
                )

        if node_count_for_XOR % 2 == 0:
            return total_score
        # one node cannot be flipped, choose the one with the smallest gain or loss
        return total_score - smallest_diff_num_to_XORed


def test():
    sol = Solution()
    res = sol.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]])
    assert res == 6
    res = sol.maximumValueSum([24, 78, 1, 97, 44], 6, [[0, 2], [1, 2], [4, 2], [3, 4]])
    assert res == 260


test()
