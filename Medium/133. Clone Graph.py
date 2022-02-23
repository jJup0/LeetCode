# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def connect_neighbors(original_node: 'Node') -> None:
            # mark as visited to not visit node twice
            self.visited.add(original_node.val)
            # create clone or get if already created
            cloned = get_clone(original_node.val)
            # set neighbors for clones
            cloned.neighbors = [get_clone(neighbor.val) for neighbor in original_node.neighbors]
            
            # keep reconstructing cloned graph with neighbors
            for neighbor in original_node.neighbors:
                if not (neighbor.val in self.visited):
                    connect_neighbors(neighbor)
        
        def get_clone(val):
            # faster than dict.setdefault as Node() does not need to be constructed and passed every time
            if not (val in self.cloned_nodes):
                self.cloned_nodes[val] = Node(val)
            return self.cloned_nodes[val]
        
        if not node:
            return None
        
        self.cloned_nodes = dict()
        self.visited = set()
        
        connect_neighbors(node)
        return self.cloned_nodes[1]