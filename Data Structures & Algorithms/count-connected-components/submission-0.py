class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build an adj list first
        # keep a res of connected components with a global_set()
        # only run bfs on ones without n
        def bfs(n, mapping, visited_set):
            que = deque([n])
            while que:
                node = que.popleft()
                visited_set.add(node)
                for neighbor in mapping[node]:
                    if neighbor not in visited_set:
                        que.append(neighbor)    
        
        mapping = defaultdict(list)
        visited_set = set()
        res = 0 
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        for i in range(n):
            if i not in visited_set:
                res += 1
                bfs(i, mapping, visited_set)
        
        return res