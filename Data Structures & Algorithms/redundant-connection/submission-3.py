class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # implement using union find for practice
        n = len(edges)
        parent = {i:i for i in range(1, n + 1)}
        rank = {i:0 for i in range(1, n + 1)}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def merge(x, y):
            nonlocal parent, rank 
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False # can't merge, they're the same
            
            # check the rank before merging
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                # equal rank
                parent[root_x] = root_y
                rank[root_y] += 1
        
        def connected(x, y):
            return find(x) == find(y)

        for edge in edges:
            x, y = edge
            if connected(x, y):
                return edge
            # otherwise we merge them together
            merge(x, y)
        return [-1, -1] # should never happen 