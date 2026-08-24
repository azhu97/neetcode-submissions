class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            print("EARLY")
            return False

        que = deque([0])
        visited = set([0])
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        while que:
            curr = que.popleft()
            print("CURR: ", curr)
            print("NGBR: ")
            for ngbr in adj_list[curr]:
                print(ngbr)
                if ngbr in visited:
                    continue
                visited.add(ngbr)
                que.append(ngbr)
        return len(visited) == n