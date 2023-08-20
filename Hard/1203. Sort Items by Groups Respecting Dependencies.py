class Node:
    def __init__(self, id: int, prerequisites: set[int] | None = None) -> None:
        self.id = id
        if prerequisites is None:
            prerequisites = set()
        self.prerequisites = prerequisites
        self.post_requisites: set[int] = set()

    @classmethod
    def topological_sort(
        cls, idxs: set[int], prerequisites: list[list[int]] | list[set[int]]
    ) -> list[int] | None:
        """
        Returns a topological sorting of the given indices, given the prerequisites.

        If there is a cycle, None is returned.
        x := sum(len(prerequisites[i]) for i in idxs)
        O(len(idxs) + x) time complexity
        O(len(idxs) + x) space complexity
        """
        nodes_in_group = {
            item: Node(item, set(b for b in prerequisites[item] if b in idxs))
            for item in idxs
        }

        sources: list["Node"] = []
        for node in nodes_in_group.values():
            if not node.prerequisites:
                sources.append(node)
            else:
                for pre in node.prerequisites:
                    nodes_in_group[pre].post_requisites.add(node.id)

        res_list: list[int] = []

        while sources:
            source_node = sources.pop()
            res_list.append(source_node.id)
            for post in source_node.post_requisites:
                nodes_in_group[post].prerequisites.remove(source_node.id)
                if not nodes_in_group[post].prerequisites:
                    sources.append(nodes_in_group[post])

        if len(res_list) < len(idxs):
            return None
        return res_list


class Solution:
    """
    There are n items each belonging to zero or one of m groups where group[i] is
    the group that the i-th item belongs to and it's equal to -1 if the i-th item
    belongs to no group. The items and the groups are zero indexed. A group can
    have no item belonging to it.

    Return a sorted list of the items such that:
    - The items that belong to the same group are next to each other in the sorted
      list.
    - There are some relations between these items where beforeItems[i] is a list
      containing all the items that should come before the i-th item in the sorted
      array (to the left of the i-th item).

    Return any solution if there is more than one solution and return an empty
    list if there is no solution.

    Constraints:
    - 1 <= m <= n <= 3 * 10^4
    - group.length == beforeItems.length == n
    - -1 <= group[i] <= m - 1
    - 0 <= beforeItems[i].length <= n - 1
    - 0 <= beforeItems[i][j] <= n - 1
    - i != beforeItems[i][j]
    - beforeItems[i] does not contain duplicates elements.
    """

    def sortItems(
        self, n: int, m: int, group: list[int], before_items: list[list[int]]
    ) -> list[int]:
        """
        Establish a valid topological order within each group, then a valid topological order between groups.
        x := sum(len(b) for b in before_items)
        O(n + x) / O(n + x)     time / space complexity
        """
        # create a mapping from each group to its nodes
        # nodes without a group a assigned a new pseudo group
        group_to_idxs_set: dict[int, set[int]] = {g: set() for g in range(m)}
        # group index to give to the next node without a group
        curr_no_group_idx = m
        for i, g in enumerate(group):
            if g == -1:
                # if no group, create a new pseudo group
                group_to_idxs_set[curr_no_group_idx] = set((i,))
                group[i] = curr_no_group_idx
                curr_no_group_idx += 1
            else:
                group_to_idxs_set[g].add(i)

        # for each group, check if a valid order for nodes within that group can be found
        group_to_idxs_ordered: dict[int, list[int]] = {}
        for g, items_set in group_to_idxs_set.items():
            ordering = Node.topological_sort(items_set, before_items)
            if ordering is None:
                return []
            group_to_idxs_ordered[g] = ordering

        # check if orderings between different groups is possible
        # find dependencies between groups
        group_to_before_groups: list[set[int]] = [
            set() for _ in range(curr_no_group_idx)
        ]
        for g, items_set in group_to_idxs_set.items():
            for item in items_set:
                for pre in before_items[item]:
                    group_to_before_groups[g].add(group[pre])
            group_to_before_groups[g].discard(g)

        ordering = Node.topological_sort(
            set(range(curr_no_group_idx)), group_to_before_groups
        )
        if ordering is None:
            return []

        # an ordering between groups is possible
        # just concatenate the order established within groups
        res: list[int] = []
        for g_idx in ordering:
            res.extend(group_to_idxs_ordered[g_idx])
        return res
