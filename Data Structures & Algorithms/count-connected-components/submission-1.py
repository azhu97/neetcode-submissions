class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # go through 0 -> n - 1 and run bfs with a SHARED visited set
        # if that n already exists in the visited set, continue
        # else increment res
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        res = 0
        visited = set()
        def bfs(node):
            nonlocal visited
            nonlocal adj_list
            if node in visited:
                return 0 
            que = deque([node])
            while que:
                curr = que.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                for ngbr in adj_list[curr]:
                    if ngbr in visited:
                        continue
                    que.append(ngbr)
            return 1
            
        for i in range(n):
            res += bfs(i)
        return res