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
        root = Node(val=node.val)
        visted = set([node.val]) # otherwise, we will bounce back and forth
        q1 = deque([node])
        q2 = deque([root]) # deep copy 
        while q1:
            node1, node2 = q1.popleft(), q2.popleft()
            visted.add(node1.val)
            for node in node1.neighbors:
                if node.val in visted:
                    continue
                # deep copy process 
                deep_copy = Node(node.val)
                # link both ways 
                node2.neighbors.append(deep_copy)
                deep_copy.neighbors.append(node2)
                # now we want to append to the stack 
                q1.append(node)
                q2.append(deep_copy)
        return root