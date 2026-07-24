from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1 and len(edges) == 0:
            return True
        # say there are n nodes
        # can i add n - 1 nodes without causing a cycle? 
        # by defination, we can rule out any tree with > n edges
        if len(edges) >= n:
            # means that there is unnessary edge
            return False
        mapping = defaultdict(list)
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        que = deque([edges[0][0]])
        visited_set = set()

        while que:
            node = que.popleft()
            visited_set.add(node)

            for neighbor in mapping[node]:
                if neighbor not in visited_set:
                    que.append(neighbor)
        
        return len(visited_set) == n