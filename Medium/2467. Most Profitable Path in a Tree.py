"""
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at
node 0. You are given a 2D integer array edges of length n - 1 where
edges[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i
in the tree.

At every node i, there is a gate. You are also given an array of even integers
amount, where amount[i] represents:
- the price needed to open the gate at node i, if amount[i] is negative, or,
- the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:
- Initially, Alice is at node 0 and Bob is at node bob.
- At every second, Alice and Bob each move to an adjacent node. Alice moves
  towards some leaf node, while Bob moves towards node 0.
- For every node along their path, Alice and Bob either spend money to open the
  gate at that node, or accept the reward. Note that:
  - If the gate is already open, no price will be required, nor will there be
    any cash reward.
  - If Alice and Bob reach the node simultaneously, they share the price/reward
    for opening the gate there. In other words, if the price to open the gate is c,
    then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c,
    both of them receive c / 2 each.
- If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches
  node 0, he stops moving. Note that these events are independent of each other.

Return the maximum net income Alice can have if she travels towards the optimal
leaf node.

Constraints:
- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 0 <= a_i, b_i < n
- a_i!= b_i
- edges represents a valid tree.
- 1 <= bob < n
- amount.length == n
- amount[i] is an even integer in the range [-10^4, 10^4].
"""

from dataclasses import dataclass, field


@dataclass
class Node:
    amount: int
    neighbors: list["Node"] = field(default_factory=list)
    parent: "Node | None" = None
    distance_to_root: int = 0

    def children_iter(self):
        return (neighbor for neighbor in self.neighbors if neighbor is not self.parent)


class Solution:
    def mostProfitablePath(
        self, edges: list[list[int]], bob: int, amounts: list[int]
    ) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        nodes: list[Node] = [Node(amount=amount) for amount in amounts]
        for a, b in edges:
            nodes[a].neighbors.append(nodes[b])
            nodes[b].neighbors.append(nodes[a])

        self._fill_in_parent_and_root_distance(nodes)
        self._clear_bobs_path(nodes[bob])
        return self._get_alice_max_profit(nodes)

    def _fill_in_parent_and_root_distance(self, nodes: list[Node]):
        # front[i] = (node, parent, distance to root)
        front: list[tuple[Node, Node, int]] = [
            (neighbor, nodes[0], 1) for neighbor in nodes[0].neighbors
        ]
        while front:
            node, parent, distance_to_root = front.pop()
            node.distance_to_root = distance_to_root
            node.parent = parent
            front.extend(
                (neighbor, node, distance_to_root + 1)
                for neighbor in node.children_iter()
            )

    def _clear_bobs_path(self, bob: Node):
        original_bob = curr_bob_node = bob
        while True:
            if curr_bob_node.distance_to_root > original_bob.distance_to_root // 2:
                # bob reaches node before alice can
                curr_bob_node.amount = 0
            elif curr_bob_node.distance_to_root == original_bob.distance_to_root / 2:
                # alice and bob meet at the same time
                curr_bob_node.amount //= 2
                break
            else:
                break
            # go to next nearest node to root
            curr_bob_node = curr_bob_node.parent
            assert curr_bob_node

    def _get_alice_max_profit(self, nodes: list[Node]):
        front: list[tuple[Node, int]] = [(nodes[0], 0)]
        result = -1_000_000_000
        while front:
            node, net_profit = front.pop()
            net_profit += node.amount
            if node.parent and len(node.neighbors) == 1:
                # leaf node
                result = max(result, net_profit)
            else:
                front.extend(
                    (neighbor, net_profit) for neighbor in node.children_iter()
                )
        return result
