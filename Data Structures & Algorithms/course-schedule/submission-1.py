from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list and starting node set
        adj_list = defaultdict(list)
        s = set()
        for u, v in prerequisites:
            s.add(u)
            if v in s:
                return False
            adj_list[u].append(v)
        
        # now run bfs
        que = deque(list(s))
        s = set()
        while que:
            node = que.popleft()
            s.add(node)
            for adj in adj_list[node]:
                if adj not in s:
                    que.append(adj)
        
        return len(s) == numCourses

        
        