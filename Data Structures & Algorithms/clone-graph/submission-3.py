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
            temp = que.popleft()
            
            for neighbor in temp.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    que.append(neighbor)
                clone[temp].neighbors.append(clone[neighbor])
    
        return clone[node]