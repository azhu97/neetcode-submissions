class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # find out which one can be removed from the graph without disconnecting
        # we can run prims algoirhtm with the edges, giving higher prior to earlier
        # then select from the remaining edges
        
        # pick any edge, keep adding 
        mapping = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            mapping[a].append((i, b))
            mapping[b].append((i, a))

        que = []
        heapq.heappush(que, (-1, 1))
        visited = set()
        used_indexes = set()
        while que and len(visited) <= n - 1:
            val, node = heapq.heappop(que)
            # print(f"current node: {node}, val: {val}")
            if node in visited:
                # print(f"skipping, node {node} in visited set")
                continue
            visited.add(node)
            used_indexes.add(val)
            for ngbr in mapping[node]:
                # print(ngbr)
                if ngbr[1] in visited:
                    # print("SKIPPING")
                    continue
                heapq.heappush(que, ngbr) # ngbr == (index, next_node)
                
        # print(visited)
        # print(used_indexes)
        for i in range(len(edges)):
            if i not in used_indexes:
                return edges[i]
        return [-1, -1]
