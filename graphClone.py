"""
cloning a graph, NOT copying. Different memory

"""


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visitedNodes = {}

        def dfs(node):
            if node in visitedNodes:
                return visitedNodes[node]
            
            copy = Node(node.val, [])
            visitedNodes[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        
        return dfs(node)
