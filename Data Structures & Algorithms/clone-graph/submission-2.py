"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clone = {node: Node(node.val)}
        que = deque([node])
        while que:
            node = que.popleft()
            
            for neighbor in node.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    que.append(neighbor)
                clone[node].neighbors.append(clone[neighbor])
    
        return clone[node]